# Bio Constitution Rules Library

A machine-readable constitutional rule library for biological dual-use content, covering 30 decision rules across six bio domains. Designed for integration with Constitutional Classifier training pipelines.

## What this is

Constitutional Classifiers (Anthropic, arXiv:2501.18837) train input/output classifiers on synthetic data generated from constitution rules. The quality of training data depends on the quality of the rules. This library provides bio-domain-specific rules authored at the biological-activity level — the level at which decisions actually differ — rather than at the generic CBRN level used in most published constitutions.

Each rule contains:
- Plain-language rule statement
- Structured JSON rule statement (for pipeline ingestion)
- Biological reasoning (why the line falls where it does)
- 2–3 edge cases with resolutions
- Resolving context table (what shifts severity up or down)
- Severity tier (one of four)
- Explicit regulatory mapping (NSABB DURC, FSAP, BWC/CWC, Australia Group, WHO)
- Example legitimate query and example concerning query

## What this is not

- No synthesis routes, recipes, or operational threat detail
- No enumeration of novel capabilities
- No information not already in the open regulatory literature
- The rules are decision criteria about research legitimacy, not instructions

## Repository structure

```
ConstitutionRules/
├── README.md                        ← this file
├── schema.json                      ← JSON Schema for rule records (draft-2020-12)
├── LICENSE                          ← Apache 2.0
├── rules/
│   ├── virology/                    ← V01–V05
│   ├── toxicology/                  ← T01–T05
│   ├── synthetic_biology/           ← S01–S05
│   ├── genomics/                    ← G01–G05
│   ├── pathogen_biology/            ← P01–P05
│   └── dual_use_chemistry/          ← C01–C05
│       (each domain: .md + .json per rule)
├── phase1/
│   ├── domain_scopes.md             ← scope contract for 6 domains
│   ├── rule_topics_master.md        ← 30-topic master table
│   └── topic_rationale.md           ← topic selection + DURC coverage audit
├── phase2/
│   └── regulatory_mapping.md        ← per-domain regulatory reference matrix
├── usage_notes.md                   ← CC pipeline integration guide
└── research/                        ← background research (read-only)
```

## The 30 rules at a glance

### Virology

| ID | Topic | Severity |
|----|-------|----------|
| V01 | Airborne transmission enhancement experiments | hard-refuse |
| V02 | Host range alteration and cross-species experiments | decline-with-alternative |
| V03 | Immune evasion mechanism characterization vs. engineering | decline-with-alternative |
| V04 | Reconstruction/reconstitution of eradicated or extinct viruses | hard-refuse |
| V05 | Vaccine antigen design and standard virological characterization | assist-with-caveats |

### Toxicology

| ID | Topic | Severity |
|----|-------|----------|
| T01 | Mechanism of action of regulated toxins | assist-with-caveats |
| T02 | Structure-activity relationships for lethality optimization | hard-refuse |
| T03 | Production scale-up and quantity thresholds | decline-with-alternative |
| T04 | Delivery mechanism and aerosol dispersal research | hard-refuse |
| T05 | Antidote, countermeasure, and detection research | assist-with-caveats |

### Synthetic Biology

| ID | Topic | Severity |
|----|-------|----------|
| S01 | De novo DNA synthesis of select agent genome sequences | hard-refuse |
| S02 | Genetic circuit design targeting pathogen characteristics | decline-with-alternative |
| S03 | Directed evolution of virulence factors or toxin potency | decline-with-alternative |
| S04 | CRISPR editing of regulated pathogens | decline-with-alternative |
| S05 | Metabolic engineering and non-pathogen synthetic biology | warn-and-assist |

### Genomics

| ID | Topic | Severity |
|----|-------|----------|
| G01 | Functional annotation of select agent genomes | decline-with-alternative |
| G02 | AI-assisted de novo design of novel dangerous pathogen sequences | hard-refuse |
| G03 | Pandemic potential prediction from viral sequence data | decline-with-alternative |
| G04 | Variant effect prediction for pathogen virulence determinants | assist-with-caveats |
| G05 | Metagenomics-based novel pathogen discovery | warn-and-assist |

### Pathogen Biology

| ID | Topic | Severity |
|----|-------|----------|
| P01 | Virulence factor characterization in regulated pathogens | assist-with-caveats |
| P02 | Virulence factor engineering for enhancement | hard-refuse |
| P03 | Antibiotic/antiviral resistance engineering and deliberate transfer | decline-with-alternative |
| P04 | Immune evasion mechanism studies | decline-with-alternative |
| P05 | Diagnostic biomarker and vaccine target identification | assist-with-caveats |

### Dual-Use Chemistry

| ID | Topic | Severity |
|----|-------|----------|
| C01 | CWC Schedule 1 compound synthesis and close structural analogs | hard-refuse |
| C02 | Schedule 2/3 precursor acquisition and sourcing patterns | decline-with-alternative |
| C03 | AI-assisted molecular design targeting toxic bioactivity | decline-with-alternative |
| C04 | Delivery system and dispersal mechanism design for chemical agents | hard-refuse |
| C05 | Reagent sourcing for routine biological research | assist-with-caveats |

## Severity tier definitions

| Tier | Meaning | Count |
|------|---------|-------|
| `hard-refuse` | Decline with no alternative; any assistance circumvents a safety layer (IGSC screening, OPCW verification, P3CO review) | 9 |
| `decline-with-alternative` | Decline the specific request; offer a substantive alternative that meets legitimate scientific needs | 12 |
| `assist-with-caveats` | Assist; include explicit caveats about FSAP status, BSL requirements, or dual-use nature | 7 |
| `warn-and-assist` | Assist; note that downstream activities may require registration or BSL-specific conditions | 2 |

## Regulatory frameworks covered

| Framework | Abbreviation | Applicable rules |
|-----------|-------------|-----------------|
| NSABB DURC Policy (2013 + 2023) | DURC | All virology, pathogen biology, synthetic biology, genomics hard-refuse and decline rules |
| Federal Select Agent Program (42 CFR Part 73) | FSAP | V01–V04, T01–T04, S01–S04, G01–G03, P01–P04 |
| WHO Laboratory Biosafety Manual 4th ed. (2020) | WHO-LBM4 | All pathogen-involving rules |
| Biological Weapons Convention (Art. I) | BWC | All hard-refuse biological rules |
| Chemical Weapons Convention (Art. II + Schedules) | CWC | C01–C04, T02, T04 |
| Australia Group Common Control Lists | AG | C01–C04, S01–S03, T01–T04 |
| IGSC Harmonized Synthesis Screening Protocol (2022) | IGSC | S01, S03, G02 |
| P3CO Framework (HHS 2017) | P3CO | V01, V02, G03 |
| NSABB 2023 extended scope (sequence-based prediction) | NSABB-2023 | G02, G03, G04 |

## JSON Schema

`schema.json` defines the rule record structure using JSON Schema draft-2020-12. Required fields:

```
rule_id, version, domain, topic, severity_tier,
rule_statement_plain, biological_reasoning,
edge_cases, example_legitimate_query, example_concerning_query
```

Validate a rule record:
```bash
# Using ajv-cli
npx ajv-cli validate -s schema.json -d rules/virology/V01_airborne_transmission.json
```

## Using the rules with a Constitutional Classifier pipeline

See `usage_notes.md` for full integration guidance. In brief:

1. **Synthetic data generation:** Each rule's `example_legitimate_query` and `example_concerning_query`, combined with the `edge_cases` array, seed the positive and negative classes for synthetic training data generation. The `biological_reasoning` field provides the grounding narrative for paraphrase generation.

2. **Severity-aware training:** The four-tier severity system supports multi-class or ordinal classifiers. Hard-refuse and decline-with-alternative rules generate clearly negative examples; assist-with-caveats rules generate the nuanced positive/caveat examples that are hardest to get right.

3. **Rule composition:** Rules in adjacent domains interact. V01 (airborne transmission) and S03 (directed evolution) can jointly fire when a query involves directed evolution of respiratory pathogen transmission. The `bwc_cwc_provisions` and `durc_categories` fields support cross-rule linkage.

## Methodology

The library was built in seven phases:

1. **Domain scoping** — defined inclusion/exclusion boundaries for 6 domains; selected 5 rule topics per domain based on frequency, ambiguity, and regulatory grounding
2. **Regulatory baseline extraction** — compiled per-domain regulatory reference tables anchoring each rule's Section 8 (Regulatory Mapping)
3. **Rule drafting** — wrote all 30 rules using the 10-field template
4. **Adversarial review** — four parallel review passes: red-team loophole finder, over-refusal auditor, regulatory accuracy auditor, cross-domain consistency auditor
5. **Cross-domain consistency pass** — aligned severity tiers for equivalent-risk scenarios across domains; documented intentional differences
6. **JSON schema and extraction** — defined formal JSON Schema; extracted rule JSON records into standalone files
7. **Training signal comparison** — 42-query pilot vs. generic CBRN baseline; bio-specific rules +30.9pp overall accuracy, +50.0pp on boundary queries; see `phase7/`

## Training signal comparison (Phase 7)

Bio-specific rules outperform a generic 5-rule CBRN baseline on a 42-query pilot test:

| Metric | Bio-Specific | Generic CBRN |
|--------|-------------|--------------|
| Overall accuracy | **95.2%** (40/42) | 64.3% (27/42) |
| Boundary query accuracy | **94.4%** (17/18) | 44.4% (8/18) |
| Over-refusal rate (legit science blocked) | **8.3%** | 33.3% |
| Under-refusal rate (harmful requests passed) | **0%** | 21.4% |

The gap is driven by two systematic generic failures: (1) inability to distinguish mechanism-of-action questions from synthesis requests (10 over-refusals), and (2) inability to recognize framing-invariant harmful requests wrapped in academic/computational framings (4 under-refusals). Details in `phase7/comparison_results.md`.

## Citation

If you use this library in research or training pipeline development:

```
Bio Constitution Rules Library (2026).
30 machine-readable constitutional rules for biological dual-use content.
Apache License 2.0.
```

## License

Apache 2.0 — see `LICENSE`.
