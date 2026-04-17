# Usage Notes — Bio Constitution Rules Library

Integration guide for Constitutional Classifier training pipelines and related applications.

---

## 1. Rule Record Format

Each rule exists in two forms in the same directory:

- `{ID}_{slug}.md` — human-readable markdown with all 10 fields
- `{ID}_{slug}.json` — standalone JSON record, validates against `schema.json`

Both are canonical. The markdown is the authoritative source; the JSON is extracted from the markdown's "Complete JSON Record" section.

---

## 2. Synthetic Training Data Generation

### Basic generation pattern

Each rule supports synthetic training data generation for Constitutional Classifiers. The minimal seed for a rule is:

```python
seed = {
    "rule_id": rule["rule_id"],
    "positive_anchor": rule["example_legitimate_query"],
    "negative_anchor": rule["example_concerning_query"],
    "severity_tier": rule["severity_tier"],
    "biological_reasoning": rule["biological_reasoning"],
    "domain": rule["domain"]
}
```

### Edge cases as additional seeds

The `edge_cases` array provides additional seeds for the nuanced region between clear positive and clear negative:

```python
for ec in rule["edge_cases"]:
    resolution_tier = ec["resolution"]  # e.g., "assist-with-caveats"
    seed_query = ec["description"]       # paraphrase into concrete query
    # generates training examples in the "boundary" region
```

Edge case resolutions may differ from the parent rule's severity tier (e.g., a hard-refuse rule may have an assist-with-caveats edge case for mechanism-of-action questions). These boundary examples are high value for training classifiers that avoid over-refusal.

### Paraphrase generation

The `biological_reasoning` field provides grounding for LLM-generated paraphrases. When prompting a language model to generate query variants, include the biological reasoning as context to ensure paraphrases remain biologically plausible.

---

## 3. Severity-Aware Classifier Design

### Four-tier label set

```python
SEVERITY_TIERS = [
    "warn-and-assist",        # 0 — proceed with notice
    "assist-with-caveats",    # 1 — proceed with explicit caveats
    "decline-with-alternative",  # 2 — decline; offer alternative
    "hard-refuse"             # 3 — decline; no alternative
]
```

### Label distribution across the 30 rules

| Tier | Count | Notes |
|------|-------|-------|
| hard-refuse | 9 | V01, V04, T02, T04, S01, G02, P02, C01, C04 |
| decline-with-alternative | 12 | V02, V03, T03, S02, S03, S04, G01, G03, P03, P04, C02, C03 |
| assist-with-caveats | 7 | V05, T01, T05, G04, P01, P05, C05 |
| warn-and-assist | 2 | S05, G05 |

The intentional asymmetry (more restrictive rules than permissive) reflects the asymmetric cost function in bio safety: a missed restriction has higher expected harm than an over-refusal.

### Multi-class vs. binary classifier

For a binary (safe/unsafe) classifier, map as:
- `warn-and-assist` + `assist-with-caveats` → safe class
- `decline-with-alternative` + `hard-refuse` → unsafe class

For severity-aware classifiers, use the four-tier labels directly as ordinal classes.

---

## 4. Cross-Rule Interaction

Some queries activate multiple rules simultaneously. The `durc_categories` and `bwc_cwc_provisions` fields support cross-rule linkage:

### High-interaction rule pairs

| Pair | Interaction | Combined severity |
|------|-------------|-------------------|
| V01 + S03 | Directed evolution of respiratory pathogen transmission | hard-refuse (V01 dominates) |
| T02 + C03 | AI molecular design for toxin potency optimization | hard-refuse (T02 dominates) |
| S01 + G02 | AI-designed genome sequence for FSAP pathogen | hard-refuse (both) |
| P02 + P03 | Virulence enhancement + resistance engineering in same pathogen | hard-refuse (P02) |
| T03 + T04 | Scale-up guidance + dispersal framing | hard-refuse (T04 escalation) |

**Composition rule:** When multiple rules fire, apply the most restrictive severity tier. The `hard-refuse` tier is non-negotiable regardless of which other rules also match.

### Domain boundary queries

Queries at domain boundaries are handled by cross-references in the resolving context tables. Key boundaries:

- **G04 → G01:** VEP applied to unannotated ORFs in select agent genomes escalates to G01 (functional annotation severity)
- **T01 → T02/T03/T04:** Mechanism-of-action queries escalate when production, optimization, or delivery framing appears
- **S03 → P02/T02:** Directed evolution escalates to hard-refuse when applied to FSAP Tier 1 virulence factors or CWC Schedule 1 toxin potency
- **G03 → V01:** Pandemic potential optimization shifts from G03 (decline) to hard-refuse when framing matches V01 enhancement territory

---

## 5. Regulatory Mapping Fields

The regulatory fields in each JSON record provide structured citations:

```json
"bwc_cwc_provisions": ["CWC_Sched_1", "CWC_Art_II_1_general_purpose_criterion"],
"australia_group_lists": ["chemical_precursors_schedule1_precursors"],
"durc_categories": ["cat1"]
```

These fields can be used to:
- Filter rules by regulatory jurisdiction (e.g., all rules implicating CWC Schedule 1)
- Build a regulatory citation index for auditing classifier decisions
- Cross-reference to primary regulatory documents for annotation provenance

### Regulatory document pointers

| Field value | Source document |
|-------------|----------------|
| `BWC_Art_I` | Biological Weapons Convention, Article I |
| `CWC_Sched_1` | Chemical Weapons Convention, Schedule 1 |
| `CWC_Art_II_9b_protective_purposes` | CWC Art. II.9(b) — protective/medical purposes explicitly permitted |
| `CWC_Art_II_1_general_purpose_criterion` | CWC Art. II.1 — general purpose criterion covers all toxic chemicals regardless of Schedule |
| `CWC_Art_II_1b_delivery_munitions` | CWC Art. II.1(b) — munitions and devices for delivery |
| `DURC_cat[1-7]` | NSABB DURC Policy (2013), 7 categories |
| `IGSC_screening_2022` | IGSC Harmonized Synthesis Screening Protocol (2022) |
| `P3CO_ePPP_framework` | HHS P3CO Framework (2017) — pandemic potential pathogen review |
| `NSABB_2023_sequence_extension` | NSABB 2023 recommendations extending DURC oversight to sequence-based predictions |

---

## 6. FSAP Possession Thresholds

Rules involving regulated toxins use `fsap_thresholds` (in milligrams) to encode regulatory quantity boundaries. These are the trigger points at which FSAP registration is required:

| Toxin | Threshold (mg) | Rules |
|-------|---------------|-------|
| Botulinum neurotoxin | 0.5 | T01, T02, T03 |
| Ricin | 100 | T01, T02, T03 |
| Abrin | 100 | T01, T02, T03 |
| Saxitoxin | 100 | T01, T02, T03 |
| Tetrodotoxin | 100 | T01, T02, T03 |
| Conotoxins | 100 | T01, T02, T03 |
| T-2 toxin | 1,000 | T01, T02, T03 |

Queries asking about quantities above these thresholds escalate to T03 (decline-with-alternative); queries involving production optimization at any quantity escalate to T03 or T04 depending on delivery framing.

---

## 7. What Is Not in This Library

This library intentionally excludes:

- **Radiation/nuclear:** Out of scope (different regulatory framework and threat model)
- **Cyberbio:** AI-assisted protein design as a tool (partially covered by G02, C03) but not the full biodesign attack surface
- **DURC Category 6** (enhance host susceptibility): No dedicated rule; addressed as edge cases in P03 and P04. Rationale in `phase1/topic_rationale.md`.
- **Non-DURC pathogens:** Rules calibrated to FSAP/DURC-listed organisms; BSL-2 work with non-listed organisms is addressed in edge cases and resolving context tables but does not generate dedicated rules
- **Gain-of-function agricultural pathogens:** USDA APHIS HPAI select agents are covered under V01/V02, but livestock-specific pathogens (FMD, ASF) are not independently represented

---

## 8. Version and Maintenance

Current version: **1.0** (April 2026)

Recommended update triggers:
- FSAP Select Agent list update (biannual review cycle)
- NSABB policy revision
- New DURC category creation
- Emergence of a new dual-use technique class requiring dedicated coverage (e.g., AI-assisted directed evolution at scale)
- Adversarial review finding a systematic gap (e.g., new loophole pattern not covered by existing edge cases)

Each rule carries a `version` field in its JSON record. Update the version on any substantive change to rule logic, edge case resolutions, or regulatory citations.
