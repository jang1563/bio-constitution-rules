---
language:
- en
license: apache-2.0
task_categories:
- text-classification
task_ids:
- multi-class-classification
tags:
- biosafety
- constitutional-ai
- dual-use
- responsible-ai
- content-moderation
- cbrn
- biology
- synthetic-data
pretty_name: Bio Constitution Rules — Training Corpus
size_categories:
- 1K<n<10K
---

# Bio Constitution Rules — Synthetic Training Corpus

A 1,063-record labeled training corpus for biological dual-use content classification, generated from 30 bio-domain constitutional rules. Dual-track labels: bio-specific (ground truth) and generic CBRN baseline. 39.3% of records diverge between the two labeling systems — these are the highest-value training examples.

**GitHub:** [jang1563/bio-constitution-rules](https://github.com/jang1563/bio-constitution-rules)  
**License:** Apache 2.0

---

## Dataset Summary

| Split | File | Records |
|-------|------|---------|
| Training (full) | `training_dataset.jsonl` | 1,063 |
| Divergence set (FP/FN only) | `divergence_set.json` | 418 |
| Pilot test set (held-out) | `pilot_test_set.json` | 42 |

**Label distribution:**
- ASSIST: 692 (65.1%)
- REFUSE: 371 (34.9%)

**Divergence rate:** 39.3% (418/1,063 records where bio-specific label ≠ generic CBRN label)

---

## Domains

| Domain | Records | Rules |
|--------|---------|-------|
| Virology | ~177 | V01–V05 |
| Toxicology | ~177 | T01–T05 |
| Synthetic Biology | ~177 | S01–S05 |
| Genomics | ~177 | G01–G05 |
| Pathogen Biology | ~177 | P01–P05 |
| Dual-Use Chemistry | ~178 | C01–C05 |

---

## Record Schema

```json
{
  "query_id": "V01-A-p001",
  "parent_seed_id": "V01-A",
  "domain": "virology",
  "rule_id": "V01",
  "query_type": "A",
  "query_text": "...",
  "bio_collapsed": "ASSIST | REFUSE",
  "bio_label": "assist-with-caveats | hard-refuse | ...",
  "generic_label": "ASSIST | REFUSE",
  "divergence_type": "FP | FN | AGREE",
  "divergence": true,
  "divergence_category": "retrospective_vs_prospective | mechanism_vs_synthesis | ..."
}
```

**Query types:**
- **A** — Legitimate queries (from `example_legitimate_query` per rule); always ASSIST
- **B** — Concerning queries (from `example_concerning_query`); usually REFUSE
- **C** — Boundary/edge-case queries (from `edge_cases`); mix of ASSIST and REFUSE

---

## Labels

### Bio-specific labels (`bio_collapsed`)
Ground truth derived from 30 bio-domain constitutional rules authored at the biological-activity level:
- `ASSIST` — Legitimate scientific information request
- `REFUSE` — Poses unacceptable biosafety risk

### Generic CBRN labels (`generic_label`)
5-rule regex baseline similar to published generic CBRN constitutions:
- `ASSIST` — No synthesis route, weaponization, or dangerous-agent signal detected
- `REFUSE` — One or more generic CBRN triggers detected

### Divergence types
- `FP` — bio=ASSIST, generic=REFUSE (over-refusal by generic baseline)
- `FN` — bio=REFUSE, generic=ASSIST (under-refusal by generic baseline)
- `AGREE` — Both systems agree

---

## Divergence Categories

The 23 categories capture the bio-specific distinctions that generic rules miss:

| Category | Description |
|----------|-------------|
| `mechanism_vs_synthesis` | Mechanism-of-action question vs. synthesis/production request |
| `retrospective_vs_prospective` | Historical/surveillance analysis vs. prospective enhancement design |
| `framing_invariance` | Academic/computational framing that does not reduce dual-use risk |
| `embedded_escalation` | Two-part query where second part escalates into enhancement request |
| `amr_surveillance_vs_engineering` | Resistance surveillance vs. deliberate resistance engineering |
| `antigen_vs_genome_synthesis` | Single antigen expression vs. full-genome synthesis |
| `host_range_characterization` | Natural host range vs. experimental expansion |
| `therapeutic_context` | Countermeasure optimization vs. weaponization/potency optimization |
| *(+ 15 others)* | See [GitHub repo](https://github.com/jang1563/bio-constitution-rules) for full list |

---

## Benchmark Results

Classifiers evaluated on the 42-query held-out pilot test set:

| System | Overall | Type C (boundary) | FP recovered | FN recovered | Cost |
|--------|---------|-------------------|-------------|-------------|------|
| Generic CBRN baseline | 52.4% (22/42) | 0/18 (0%) | 0/9 | 0/11 | $0 |
| Few-shot retrieval (Phase 9) | **100.0%** (42/42) | 18/18 (100%) | 9/9 | 11/11 | $0.025 |
| Fine-tuned gpt-4o-mini (Phase 10D) | **97.6%** (41/42) | 17/18 (94%) | 9/9 | 10/11 | ~$2 |

5-fold seed-level cross-validation on this corpus: **86.7%** overall (+26pp over generic baseline).

---

## Generation Methodology

1. **Seeds** — 142 seed queries extracted from 30 rule JSON files (example queries + edge cases)
2. **Paraphrases** — Claude Haiku (`claude-haiku-4-5-20251001`) generated 6–8 paraphrase variants per seed with persona, specificity, and purpose-framing variation; quality-gate filtered (length, near-duplicate, failed-generation checks)
3. **Bio labeling** — Inherited from parent seed's rule severity tier
4. **Generic labeling** — 5-rule priority-ordered regex baseline
5. **Divergence extraction** — Records where bio ≠ generic, annotated with divergence category

---

## Intended Use

- Constitutional Classifier training data for biological dual-use content
- Few-shot retrieval context for in-context classification
- Fine-tuning base model classifiers on biosafety decisions
- Benchmarking generic vs. bio-specific CBRN rule quality

---

## What This Dataset Does NOT Contain

- No synthesis routes, recipes, or operational threat detail
- No enumeration of novel dangerous capabilities
- No information not already in the open regulatory literature
- Queries are about research legitimacy decisions, not operational instructions

---

## Regulatory Frameworks Covered

NSABB DURC (2013 + 2023), FSAP (42 CFR Part 73), WHO Laboratory Biosafety Manual 4th ed. (2020), Biological Weapons Convention (Art. I), Chemical Weapons Convention (Art. II + Schedules), Australia Group Common Control Lists, IGSC Harmonized Synthesis Screening Protocol (2022), P3CO Framework (HHS 2017)

---

## Citation

```
Bio Constitution Rules Library (2026).
30 machine-readable constitutional rules for biological dual-use content.
Apache License 2.0.
https://github.com/jang1563/bio-constitution-rules
```
