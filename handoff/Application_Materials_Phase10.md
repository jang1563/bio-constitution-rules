# Application Materials — Bio Constitution Rules Library (Phases 1–10)

Updated after Phase 10 completion (2026-04-19). Use these to update CV and cover letter for the Anthropic Bio Safety Research Scientist application (Job ID 5066977008).

---

## CV Bullet Points

### Under "Portfolio / Artifacts" or "Selected Projects"

**Bio Constitution Rules Library** (Apr 2026) — [github.com/jang1563/bio-constitution-rules](https://github.com/jang1563/bio-constitution-rules)
- Authored 30 machine-readable constitutional rules across 6 bio domains (virology, toxicology, synthetic biology, genomics, pathogen biology, dual-use chemistry), each with biological reasoning, 3 edge cases, resolving-context table, 4-tier severity tier, and explicit regulatory mapping (NSABB DURC, FSAP, BWC/CWC, Australia Group, WHO LBM 4th ed.)
- Built end-to-end Constitutional Classifier pipeline: 1,063-record synthetic training corpus → TF-IDF retrieval → Claude Haiku few-shot classifier → **100% accuracy** on 42-query pilot, correcting all 9 FP over-refusals and 11 FN under-refusals vs. 52.4% generic CBRN baseline (+47.6pp)
- Validated generalization via 5-fold seed-level cross-validation: **86.7% overall** (922/1,063), +26pp over generic baseline; adversarial robustness testing across 4 transform types (roleplay, authority claim, hypothetical distancing, euphemistic substitution): **92.9–97.6% accuracy** under adversarial framing
- JSON format ready for Constitutional Classifier pipeline ingestion; Apache 2.0 license

### Shorter single-line version (for table-format CV)

> Bio Constitution Rules Library: 30 bio-domain constitutional rules → 1,063-record training corpus → 100% pilot accuracy, 86.7% 5-fold CV, 92.9–97.6% adversarial robustness. [GitHub](https://github.com/jang1563/bio-constitution-rules)

---

## Cover Letter Paragraphs

### Option A — Full technical paragraph (for longer cover letters)

> As a concrete demonstration of how I would contribute, I have built a Bio Constitution Rules Library directly compatible with Anthropic's Constitutional Classifier training pipeline. The library comprises 30 machine-readable constitutional rules across six biological domains — virology, toxicology, synthetic biology, genomics, pathogen biology, and dual-use chemistry — each authored at the biological-activity level with explicit reasoning for where decision lines fall, realistic edge cases, and regulatory anchoring to NSABB DURC, FSAP, BWC/CWC, Australia Group, and WHO Laboratory Biosafety Manual frameworks. I then used these rules to generate a 1,063-record synthetic training corpus and evaluated a TF-IDF retrieval + Claude Haiku few-shot classifier against a 42-query pilot held out from training. The bio-specific classifier achieves 100% accuracy — correcting every error the generic CBRN baseline makes, including all 9 false-positive over-refusals and 11 false-negative under-refusals. Generalization is validated by 5-fold seed-level cross-validation (86.7% overall, +26pp over generic baseline) and adversarial robustness testing across four framing attacks (92.9–97.6% accuracy). The complete pipeline is open-source at [github.com/jang1563/bio-constitution-rules](https://github.com/jang1563/bio-constitution-rules).

### Option B — Compact paragraph (2-3 sentences)

> I have built and benchmarked a Bio Constitution Rules Library directly compatible with Anthropic's Constitutional Classifier pipeline: 30 machine-readable bio-domain rules → 1,063-record synthetic training corpus → 100% accuracy on a 42-query pilot (+47.6pp over generic CBRN baseline), with 86.7% 5-fold cross-validation accuracy and 92.9–97.6% adversarial robustness across roleplay, authority-claim, hypothetical, and euphemistic framings. Each rule is authored at the biological-activity level with explicit reasoning, edge cases, and NSABB/FSAP/BWC/CWC regulatory anchoring. The full pipeline is open-source under Apache 2.0.

### Option C — One-sentence mention (for tight word limits)

> I have open-sourced a 30-rule bio-domain constitutional library with a working classifier achieving 100% pilot accuracy and 86.7% cross-validated generalization ([github.com/jang1563/bio-constitution-rules](https://github.com/jang1563/bio-constitution-rules)).

---

## Interview Talking Points

### What this demonstrates

1. **Domain expertise translating to operational artifacts** — Not just knowing bio, but encoding bio-specific decision logic into a form a classifier can learn from. The generic CBRN baseline fails *all* 18 boundary queries (Type C, 0% accuracy); the bio-specific training corpus enables 100% accuracy on those same queries.

2. **The four distinctions generic rules cannot make** — Ready to explain each with concrete examples from the pilot:
   - Mechanism-of-action vs. synthesis requests (10 FP cases)
   - Retrospective surveillance vs. prospective enhancement design (FP + FN cases)
   - Framing-invariant harmful requests wrapped in academic/computational language (FN cases)
   - Embedded escalation in two-part queries (FN cases)

3. **Adversarial framing invariance** — The system prompt explicitly encodes the framing-invariance principle ("The framing of a request does not change the underlying safety decision"). Result: 97.6% accuracy under authority claims, hypothetical distancing, and euphemistic substitution. Roleplay/fiction is the hardest attack (92.9%).

4. **Identified weak spots** — CHE-003 (thiodiglycol export-compliance query) is the consistent failure point across adversarial conditions; VIR-004 (H5N1 surveillance) and PAT-004 (anthrax virulence factor characterization) degrade under roleplay framing. Honest about limitations.

5. **Cost-efficiency** — 42-query pilot evaluation: $0.025. Full 1,063-record cross-validation: $0.61. Adversarial eval (168 API calls): $0.089. Total Phase 7–10 API cost: ~$0.75.

### Likely questions and answers

**Q: Why TF-IDF retrieval rather than embedding-based retrieval?**  
A: Interpretability and cost. TF-IDF retrieval is deterministic, requires no embedding API calls, and retrieval quality (mean top-1 cosine similarity 0.44) is sufficient for this vocabulary. Embedding retrieval would improve recall on paraphrase-heavy test queries but adds latency and cost. For a classifier demo, TF-IDF proves the training signal is real without confounding by retrieval quality.

**Q: Would this scale to a production Constitutional Classifier?**  
A: The training corpus (1,063 records) is a seed, not a production dataset. Production would require (1) more paraphrase diversity, (2) human expert review of the divergence set (418 FP/FN records), (3) fine-tuning rather than few-shot inference, and (4) out-of-distribution evaluation on real query logs. The value of this work is demonstrating that the bio-specific rule structure encodes signal that generic rules don't — the training corpus is a proof-of-concept for that claim.

**Q: How did you determine severity tiers?**  
A: Anchored to regulatory frameworks: hard-refuse maps to activities requiring P3CO review or IGSC screening (9 rules); decline-with-alternative maps to FSAP-regulated or DURC-adjacent activities (12 rules); assist-with-caveats maps to activities with dual-use potential but legitimate primary use (7 rules); warn-and-assist maps to standard research with downstream regulatory implications (2 rules). Cross-domain consistency pass aligned equivalent-risk scenarios across domains.

**Q: What would you add if you had 4 more weeks?**  
A: (1) Human expert review of the 418 divergence-set records — the highest-value training signal; (2) fine-tuning rather than few-shot to test whether the signal holds at lower k; (3) out-of-distribution evaluation on queries outside the 6 domains; (4) expand adversarial testing to multi-turn conversations where the harmful intent emerges only in context.

---

## Key Numbers Summary

| Metric | Value |
|--------|-------|
| Rules authored | 30 (6 domains × 5 rules) |
| Severity tiers | 4 (hard-refuse: 9, decline-with-alt: 12, assist-with-caveats: 7, warn-and-assist: 2) |
| Regulatory frameworks | 9 (NSABB DURC, FSAP, WHO-LBM4, BWC, CWC, Australia Group, IGSC, P3CO, NSABB-2023) |
| Training corpus | 1,063 records (6 domains, dual-track bio + generic labels) |
| Divergence set | 418 records (39.3% divergence rate) |
| Pilot accuracy (Phase 9) | 100% (42/42) vs. 52.4% generic baseline |
| FP corrected | 9/9 (100%) |
| FN corrected | 11/11 (100%) |
| 5-fold CV accuracy (Phase 10A) | 86.7% (922/1,063), +26pp vs. generic |
| Adversarial accuracy (Phase 10B) | 92.9–97.6% across 4 transform types |
| Total API cost (Phases 7–10) | ~$0.75 |
| GitHub | github.com/jang1563/bio-constitution-rules |
| License | Apache 2.0 |
