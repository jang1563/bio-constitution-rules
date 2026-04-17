# Phase 7 — Training Signal Comparison

## Summary

Bio-specific constitutional rules outperform a generic CBRN baseline by **+30.9 percentage points overall** and **+50.0 percentage points on boundary queries** in a 42-query pilot test.

| System | Overall accuracy | Boundary (Type C) accuracy | Over-refusal rate |
|--------|-----------------|---------------------------|-------------------|
| Bio Constitution Rules Library | 40/42 (95.2%) | 17/18 (94.4%) | 1/12 (8.3%) |
| Generic CBRN Baseline | 27/42 (64.3%) | 8/18 (44.4%) | 4/12 (33.3%) |

## Files

| File | Description |
|------|-------------|
| `methodology.md` | Comparison design, query typology, scale-up plan |
| `generic_baseline.md` | The 5-rule generic CBRN baseline with known limitations |
| `pilot_test_set.json` | 42 labeled queries (7/domain × 6 domains) with gold labels and generic labels |
| `comparison_results.md` | Full analysis with per-query breakdown for all divergences |

## Key finding

The improvement is concentrated in two failure modes of the generic baseline:

**Over-refusal (FP, n=10):** Generic rules refuse legitimate science because they cannot apply the mechanism-of-action/synthesis distinction (CWC Art. II.9(b)), the retrospective/prospective surveillance distinction (NSABB 2023), or the single-gene/full-genome distinction (S01). Examples: VX mechanism for antidote development, ricin for cancer immunotoxin, SARS-CoV-2 natural variant surveillance.

**Under-refusal (FN, n=4):** Generic rules assist harmful requests wrapped in academic, computational, or purpose-specific framing, because they lack explicit framing-invariance logic. Examples: H5N1 serial passage experiment framed as dissertation research, pandemic potential optimization framed as "computational only," directed evolution of anthrax lethal factor framed as protein engineering coursework.

## What this means for Constitutional Classifier training

The 15 divergence queries are the high-value training examples: cases where a classifier trained on bio-specific rules learns the correct label, while one trained on generic rules learns the wrong label. At scale (100-500 examples/domain), the expected divergence set is ~300-700 examples concentrated in the mechanism/surveillance/framing-invariance regions — exactly the region where bio safety classifiers currently exhibit the highest error rates.
