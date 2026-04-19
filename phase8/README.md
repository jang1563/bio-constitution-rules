# Phase 8 — Synthetic Training Dataset

Full-scale labeled training corpus for Constitutional Classifier development, produced by applying the Phase 7 methodology to all 30 bio-domain rules at scale.

---

## Dataset Summary

| Metric | Value |
|--------|-------|
| Seeds | 142 (28 Type A · 24 Type B · 90 Type C) |
| Paraphrases generated | 956 |
| Training records | **1,063** |
| Ambiguous set | 35 |
| Divergence set | **418 (39.3%)** |
| — FP (over-refusals) | 265 |
| — FN (under-refusals) | 153 |
| Generation model | claude-haiku-4-5-20251001 |
| Generation runtime | 129.4 s |
| Pilot reproduction (Check A) | **42/42 (100%)** |

---

## Domain Distribution

| Domain | Total | FP | FN | AGREE |
|--------|-------|----|----|-------|
| virology | 186 | 29 | 23 | 134 |
| toxicology | 172 | 65 | 17 | 90 |
| synthetic_biology | 179 | 8 | 36 | 135 |
| genomics | 186 | 40 | 27 | 119 |
| pathogen_biology | 163 | 74 | 22 | 67 |
| dual_use_chemistry | 177 | 49 | 28 | 100 |
| **Total** | **1,063** | **265** | **153** | **645** |

---

## Files

| File | Records | Description |
|------|---------|-------------|
| `seeds.json` | 142 | Seed queries extracted from 30 rule JSON files |
| `paraphrases.json` | 956 | Paraphrase variants (post quality gates) |
| `paraphrases_bio_labeled.json` | 1,098 | Bio-specific labels applied |
| `paraphrases_generic_labeled.json` | 1,098 | Generic CBRN baseline labels applied |
| `training_dataset.json` | 1,063 | Final labeled training records (non-ambiguous) |
| `training_dataset.jsonl` | 1,063 | Same, JSONL format for fine-tuning pipelines |
| `divergence_set.json` | 418 | High-value FP/FN records with divergence metadata |
| `ambiguous_set.json` | 35 | Records from 5 ambiguous edge case seeds |
| `dataset_stats.json` | — | Aggregate metrics |

---

## Methodology

### Step 1 — Seed Extraction (`extract_seeds.py`)

Extracts 142 seed queries from all 30 rule JSON files across 6 domains:

- **Type A** (28 seeds): `example_legitimate_query` per rule — legitimate scientific questions on dual-use topics. Severity tier mapped via `LEGIT_TIER_FOR_RULE` (hard-refuse rules → assist-with-caveats).
- **Type B** (24 seeds): `example_concerning_query` or `example_boundary_query` (P01) per rule — requests that cross dual-use thresholds.
- **Type C** (90 seeds): `edge_cases[n].description` per rule — boundary cases where context determines permissibility.

Rules missing A seeds: C05, P05. Rules missing B seeds: C05, G05, P05, S05, T05, V05.
Five ambiguous Type C seeds (unresolvable resolution strings) routed to `ambiguous_set.json`: P01-EC3, P02-EC1, S01-EC3, T02-EC3, T05-EC3.

### Step 2 — Paraphrase Generation (`generate_paraphrases.py`)

Claude Haiku generates N paraphrase variants per seed (N=8 for Type A/B, N=6 for Type C) with temperature=1.0, varying persona, specificity, and stated purpose. Quality gates applied inline:

- **Gate 1**: Length filter (15–150 words)
- **Gate 2**: Near-duplicate within seed group (trigram Jaccard > 0.60)
- **Gate 3**: Failed generation (non-JSON output, refusal phrases)
- **Gate 4**: Global exact-duplicate removal (Step 5)

All 956 generated paraphrases passed gates (0% rejection rate).

### Step 3 — Bio Labeling (`label_bio_rules.py`)

Label inheritance: paraphrases receive parent seed's `severity_tier` and `bio_collapsed` (ASSIST/REFUSE/AMBIGUOUS). Seed records themselves are included as training examples (`is_seed=True`). Ambiguous seeds (5) produce 35 records routed to `ambiguous_set.json`.

### Step 4 — Generic Baseline Labeling (`label_generic_baseline.py`)

5-rule generic CBRN regex baseline applied to all records. Reproduces the naive classifier error modes identified in Phase 7:

| Rule | Trigger | Suppressible? |
|------|---------|---------------|
| GEN-01 | Synthesis/production route patterns | Yes (historical framing only) |
| GEN-02 | Weaponization/delivery · CW Schedule 1 agents · AChE inhibitor phrasing | No |
| GEN-03 | CW Schedule 1 agent names (VX/sarin/tabun/novichok/thiodiglycol) | No |
| GEN-04 | Pandemic potential optimization · dangerous agent names without context | Yes (mechanism/therapeutic/retrospective suppressors) |
| GEN-05 | Default | — |

**Known error modes (by design):**
- FP over-refusals (265): generic rule fires on dangerous agent names even in legitimate research context (therapeutic use, retrospective surveillance, computational-only framing, educational/annotative queries)
- FN under-refusals (153): generic rule misses embedded escalation, framing-invariant requests, and chassis-identity elevation signals

### Step 5 — Dataset Build (`build_training_dataset.py`)

Merges bio and generic labels, computes divergence type (FP/FN/AGREE), maps to divergence categories by rule ID, links to pilot analogs from Phase 7, and splits into final output files.

### Step 6 — Validation (`validate_dataset.py`)

Three checks all pass:

- **Check A** — Pilot reproduction: 42/42 Phase 7 pilot queries reproduced by `label_generic_baseline()`. Validates regex implementation against hand-labeled ground truth.
- **Check B** — Seed label integrity: all 137 seed records have correct `bio_collapsed` labels matching `seeds.json`.
- **Check C** — Distribution sanity: divergence rate 39.3% (target 25–45%), all 6 domains ≥120 records, ambiguous set 35 records (target 25–45).

---

## Record Schema

```json
{
  "query_id": "V01-A-p003",
  "parent_seed_id": "V01-A",
  "rule_id": "V01",
  "domain": "virology",
  "query_type": "A",
  "severity_tier": "assist-with-caveats",
  "bio_collapsed": "ASSIST",
  "bio_label": "assist-with-caveats",
  "bio_rule_fired": "V01",
  "bio_reasoning": "inherited_from_seed:V01-A",
  "query_text": "...",
  "is_seed": false,
  "generation_model": "claude-haiku-4-5-20251001",
  "generic_label": "REFUSE",
  "generic_rule_fired": "GEN-04",
  "generic_reasoning": "Dangerous agent name present without suppressor context",
  "divergence": true,
  "divergence_type": "FP",
  "divergence_category": "retrospective_vs_prospective",
  "pilot_analog": "VIR-004",
  "seed_query_text": "...",
  "review_status": "pending",
  "reviewer_label": null,
  "reviewer_notes": null
}
```

---

## Using the Dataset

**Training a Constitutional Classifier:**
```python
import json

training = [json.loads(l) for l in open("training_dataset.jsonl")]

# Binary classification target
examples = [
    {"text": r["query_text"], "label": 1 if r["bio_collapsed"] == "REFUSE" else 0}
    for r in training
]

# High-value divergence examples (where bio-specific rules outperform generic)
divergence = [r for r in training if r["divergence"]]
fp_examples = [r for r in divergence if r["divergence_type"] == "FP"]  # 265 over-refusals
fn_examples = [r for r in divergence if r["divergence_type"] == "FN"]  # 153 under-refusals
```

**Divergence set for contrastive training:**
The 418 divergence records (39.3%) represent cases where bio-specific constitutional rules disagree with a generic CBRN baseline. These are the highest-signal training examples — they teach the classifier the contextual nuances that distinguish legitimate dual-use research from harmful requests.

**Relationship to Phase 7:**
Phase 7 validated the methodology on 42 pilot queries (bio accuracy 95.2% vs. generic 64.3%, divergence rate 35.7%). Phase 8 scales to 1,063 labeled records at 39.3% divergence — consistent with the pilot signal.

---

## Divergence Categories

| Category | Rules | Description |
|----------|-------|-------------|
| `retrospective_vs_prospective` | V01, V04, G03 | Natural variant characterization vs. enhancement design |
| `mechanism_vs_synthesis` | T01, T02, C01 | Mechanism of action vs. synthesis route |
| `amr_surveillance_vs_engineering` | P03 | Natural resistance monitoring vs. deliberate engineering |
| `antigen_vs_genome_synthesis` | S01 | Single antigen expression vs. full-genome reconstruction |
| `clinical_vs_enhancement_vep` | G04 | Drug resistance monitoring vs. resistance engineering |
| `framing_invariance` | V03, S03, G02 | Academic framing does not resolve dual-use concern |
| `embedded_escalation` | P02, T05 | Two-part queries where second part escalates |
| `precursor_combination_logic` | C02 | Precursor combination context |
| `therapeutic_context` | C03 | Therapeutic vs. weaponization framing |
| `host_range_characterization` | V02 | Natural host range vs. experimental expansion |
| `chassis_organism_identity` | S02 | Innocuous circuit in dangerous chassis |
| `characterization_vs_enhancement_boundary` | P01 | Virulence factor characterization vs. enhancement |

---

## Cost

- Model: `claude-haiku-4-5-20251001`
- 142 API calls, ~147K total tokens
- Estimated cost: ~$0.11 USD
- Runtime: 129.4 seconds
