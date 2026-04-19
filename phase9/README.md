# Phase 9 — Few-Shot Retrieval Classifier Evaluation

Closes the end-to-end loop: **Rules → Synthetic Training Data → Working Classifier**.

A TF-IDF retrieval system pulls the 5 most similar labeled examples from the Phase 8 training corpus (1,063 records), then prompts Claude Haiku with those examples to classify each of the 42 Phase 7 pilot queries. The classifier achieves **100% accuracy** on all query types, correcting every divergence case the generic CBRN baseline missed.

---

## Results

| System | Overall | Type A (12) | Type B (12) | Type C (18) | FP corrected | FN corrected |
|--------|---------|------------|------------|------------|-------------|-------------|
| Generic CBRN baseline | **52.4%** (22/42) | 10/12 (83.3%) | 12/12 (100%) | 0/18 (0%) | 0/9 | 0/11 |
| Few-shot retrieval (Phase 9) | **100.0%** (42/42) | 12/12 (100%) | 12/12 (100%) | 18/18 (100%) | 9/9 | 11/11 |

**+47.6pp improvement overall. +100pp on boundary (Type C) queries.**

The 20 queries the generic baseline gets wrong are exactly the queries the few-shot classifier gets right. There are no regressions.

---

## What This Demonstrates

The generic 5-rule CBRN baseline (64.3% in Phase 7, 52.4% from pilot data) fails all 18 boundary queries (Type C) because it cannot distinguish:

- **Mechanism of action** from synthesis requests (10 FP over-refusals)
- **Framing-invariant harmful requests** embedded in academic/computational language (4 FN under-refusals)
- **Retrospective surveillance** from prospective enhancement design (FP + FN)
- **Embedded escalation** in two-part queries (FN)

The Phase 8 training data encodes exactly this contextual signal. When five similar labeled examples are retrieved and presented as context, Claude correctly applies the bio-specific decision logic to all 42 queries — including every boundary case.

---

## Per-Domain Improvement

| Domain | Generic | Classifier | Queries improved |
|--------|---------|-----------|-----------------|
| Virology | 4/7 (57.1%) | 7/7 (100%) | VIR-003, VIR-004, VIR-005 |
| Toxicology | 4/7 (57.1%) | 7/7 (100%) | TOX-003, TOX-004, TOX-005 |
| Synthetic Biology | 4/7 (57.1%) | 7/7 (100%) | SYN-003, SYN-004, SYN-005 |
| Genomics | 3/7 (42.9%) | 7/7 (100%) | GEN-002, GEN-003, GEN-004, GEN-005 |
| Pathogen Biology | 4/7 (57.1%) | 7/7 (100%) | PAT-003, PAT-004, PAT-005 |
| Dual-use Chemistry | 3/7 (42.9%) | 7/7 (100%) | CHE-002, CHE-003, CHE-004, CHE-005 |

---

## Methodology

### Retrieval

**TF-IDF with bigrams** (`ngram_range=(1,2)`, `max_features=10000`, `sublinear_tf=True`) fit on all 1,063 Phase 8 training records. Cosine similarity used to retrieve the top `k=5` most similar training examples per pilot query. Retrieval is **domain-blind** — the classifier must generalize across domains, not just match domain keywords.

Retrieval quality: mean top-1 similarity = 0.44 across pilot queries. All queries had at least one retrieved example with similarity > 0.20, indicating the vocabulary overlap is sufficient for meaningful retrieval.

### Few-Shot Prompt

Each pilot query is classified with a prompt containing:
1. A system message defining the two classes and four key decision criteria
2. Five retrieved training examples, each with: query text, `bio_collapsed` label, one-sentence reasoning derived from the `divergence_category` field
3. The test query

The reasoning sentences encode the bio-specific decision logic without revealing operational detail. For example, a `retrospective_vs_prospective` example includes: *"retrospective analysis of natural or published variants vs. prospective enhancement design."*

### Classification

- Model: `claude-haiku-4-5-20251001` (consistent with Phase 8 generation)
- Temperature: 0.0 (deterministic, reproducible)
- Max tokens: 10 (binary output: "ASSIST" or "REFUSE")
- Concurrency: 10 parallel requests

### Cost

| Metric | Value |
|--------|-------|
| Total input tokens | 29,131 |
| Total output tokens | 370 |
| Total cost | ~$0.025 USD |
| Runtime | 27.2 seconds |

---

## Relationship to Phase 7

Phase 7 established that bio-specific rules achieve 95.2% accuracy (40/42) vs. 64.3% (27/42) for the generic baseline on the pilot set — a hand-labeled comparison based on an early version of the generic regex. Phase 9 evaluates against the finalized pilot data (52.4% generic, 100.0% retrieval classifier) using the same 42-query test set held out from Phase 8 training data generation.

The few-shot retrieval classifier **matches and exceeds** what the full bio-specific rule application achieves, demonstrating that the Phase 8 synthetic training corpus successfully encodes the bio-specific decision signal.

---

## Files

| File | Description |
|------|-------------|
| `eval_classifier.py` | Evaluation script (TF-IDF retrieval + Claude Haiku classification) |
| `results.json` | Full per-query results, retrieval metadata, aggregate metrics |
