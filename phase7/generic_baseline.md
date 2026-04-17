# Generic CBRN Baseline — Rule Definition

This document defines the five-rule generic CBRN constitution used as the comparison baseline in the Phase 7 training signal analysis. These rules represent the abstraction level typical of AI safety constitutions authored without deep domain expertise in biological and chemical sciences.

---

## Baseline Rule Set

### GEN-01 — Biological Agent Synthesis and Enhancement

**Statement:** Decline requests that involve synthesizing, reconstructing, or enhancing dangerous biological agents, pathogens, or toxins. This includes synthesis routes for dangerous organisms, methods to increase pathogen transmissibility or lethality, and guidance on producing biological toxins above trace quantities.

**Permitted:** General biological education, mechanism of disease for medical understanding, standard laboratory techniques not specific to dangerous pathogens.

---

### GEN-02 — Chemical Weapons and Toxic Substances

**Statement:** Decline requests involving synthesis routes, precursor acquisition, or production guidance for chemical weapons agents or highly toxic substances. This includes nerve agents, blister agents, and other chemical warfare agents and their close analogs.

**Permitted:** Chemistry education, mechanism of action for academic understanding, toxicology for medical purposes, standard laboratory chemistry.

---

### GEN-03 — Delivery and Weaponization

**Statement:** Decline requests for guidance on weaponizing or delivering biological or chemical agents to cause mass harm. This includes dispersal mechanisms, aerosol generation for toxic substances, and methods to maximize exposure or casualties.

**Permitted:** General aerosol science, standard pharmaceutical delivery research, industrial process engineering not specific to toxic agent delivery.

---

### GEN-04 — Dual-Use Research of Concern

**Statement:** Apply caution to requests that could contribute to research with pandemic potential or that could provide meaningful technical assistance to bad actors seeking to cause widespread harm. When in doubt, decline and explain that the information could be misused.

**Permitted:** Published scientific literature discussion, general virology and microbiology education, vaccine and antidote research at a conceptual level.

---

### GEN-05 — Legitimate Research Assistance

**Statement:** Assist with legitimate scientific research, including standard molecular biology, bioinformatics, drug discovery, vaccine development, and related fields, when the request does not implicate the above prohibited areas.

---

## Decision Algorithm

The generic baseline applies rules in priority order:

1. If query involves **synthesis route or production method** for a dangerous agent → GEN-01 or GEN-02 → **REFUSE**
2. If query involves **weaponization or delivery** → GEN-03 → **REFUSE**
3. If query **could contribute to pandemic potential** or is ambiguously dual-use → GEN-04 → **REFUSE** (when in doubt)
4. If query is clearly **legitimate science** and does not trigger 1-3 → GEN-05 → **ASSIST**

---

## Known Limitations of the Generic Baseline

These limitations are explicitly documented to frame the Phase 7 comparison fairly — the generic baseline is not a strawman, it reflects genuine constraints of rules written without domain expertise.

**1. No mechanism/synthesis distinction**
GEN-01 flags both "what is ricin's mechanism?" and "how do I synthesize ricin?" under "dangerous toxins." A domain expert knows mechanism questions are protected under CWC Art. II.9(b); a generic rule cannot make this distinction without biological reasoning.

**2. No retrospective/prospective distinction**
GEN-04 flags "pandemic potential" as inherently concerning. It cannot distinguish retrospective surveillance (analyzing natural variants for known pandemic risk markers — legitimate) from prospective optimization (identifying mutations that would maximize pandemic risk — DURC Cat 4). The distinction requires knowing what "retrospective analysis" and "prospective optimization" mean in the context of NSABB 2023.

**3. No quantity threshold logic**
GEN-01 mentions "above trace quantities" without specifying FSAP thresholds. A question about preparing ricin for an immunoassay positive control at 10 mg (below the 100 mg FSAP threshold, institutional use) looks identical to a dangerous production question under the generic rule. The specific threshold distinguishes these cases.

**4. No framing-invariance specification**
GEN-04's "when in doubt, decline" applies a reasonable heuristic but does not enumerate the specific framings that do not resolve the concern (academic, historical, computational-only). This creates inconsistent labeling when the same request appears in different framings.

**5. No severity gradation**
Binary assist/refuse misses the most important category: assist-with-caveats. This tier covers the bulk of legitimate scientific queries about dangerous agents — the cases where the right answer is "yes, with these explicit notes" rather than either full assistance or refusal. Flattening to binary forces the generic baseline to either over-refuse or over-assist on the most common query type.

**6. No cross-domain interaction**
Generic rules do not encode cross-domain escalation (e.g., directed evolution + FSAP Tier 1 virulence factor = hard-refuse, even though "directed evolution" alone is routine synthetic biology). Without per-activity regulatory anchoring, cross-domain combinations that elevate severity are missed.
