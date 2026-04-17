# G05 — Metagenomics-Based Novel Pathogen Discovery

**Domain:** Genomics
**Severity Tier:** Warn-and-assist
**Primary DURC Category:** BSL conditional (post-discovery if isolated); DURC if isolated and meets criteria

---

## 1. Rule ID and Domain

- **Rule ID:** G05
- **Domain:** Genomics
- **Topic:** Metagenomics-based novel pathogen discovery

---

## 2. Rule Statement (Plain Language)

Assist with metagenomics analysis, bioinformatics assembly, taxonomic classification, and novel pathogen discovery from environmental and clinical samples; apply a warning when queries involve downstream characterization planning for novel agents with pandemic potential, and escalate to more restrictive rules when isolation, enhancement, or functional characterization of novel dangerous agents is proposed.

---

## 3. Rule Statement (JSON)

```json
{
  "rule_id": "G05",
  "domain": "genomics",
  "action": "warn-and-assist",
  "condition": "query involves metagenomics analysis, bioinformatics assembly, taxonomic classification, or novel pathogen discovery",
  "warning_triggers": ["novel agent with predicted pandemic potential features discovered", "downstream isolation planning for novel dangerous agent", "functional characterization proposed for novel RG3-4 candidate"],
  "escalate_when": "isolation, enhancement, or synthesis of novel dangerous agent is proposed"
}
```

---

## 4. Biological Reasoning

Metagenomics — sequencing all genetic material from an environmental or clinical sample without prior culture — is one of the most powerful tools in modern pathogen surveillance and discovery. The identification of novel coronaviruses in bat populations, the characterization of the gut virome in human health, and the discovery of novel bacterial pathogens in outbreak contexts all depend on metagenomics workflows that are unambiguously beneficial.

The dual-use concern in metagenomics is downstream, not upstream. Detecting the presence of a novel coronavirus with SARS-related spike protein features in a bat guano sample is public health surveillance — it should be encouraged, published, and acted upon through WHO reporting channels. The DURC concern emerges if and when: (a) the novel agent is proposed for isolation from the metagenomic sample; (b) the full-genome sequence is proposed for de novo synthesis; or (c) the novel agent, once isolated, is proposed for functional enhancement studies.

WHO LBM4 4th edition's risk-based framework applies precisely here: a novel pathogen discovered by metagenomics does not have a fixed risk group until it is characterized. The risk group is determined by risk assessment after characterization. The appropriate response is to assist with the metagenomics discovery phase (warn-and-assist with informational notes about downstream biosafety assessment) and escalate to more restrictive rules when downstream isolation or enhancement is proposed.

---

## 5. Edge Cases

**Edge Case 1 — Environmental bat coronavirus metagenomics for pandemic preparedness:**
A virologist asks about bioinformatics approaches for assembling novel coronavirus genomes from bat guano metagenomic samples for surveillance purposes. Resolution: **Warn-and-assist** — provide metagenomics assembly guidance; note that if near-complete coronavirus genomes with SARS-related features are assembled, WHO/NCBI reporting and institutional biosafety assessment are recommended before downstream work.

**Edge Case 2 — Clinical wastewater metagenomics for public health surveillance:**
A public health researcher asks about detecting novel pathogen sequences in wastewater surveillance metagenomics for early outbreak detection. Resolution: **Assist-with-caveats** — wastewater surveillance is a paradigmatic public health application; no dual-use concern at the detection level; note that sequences matching controlled-access pathogen databases should be reported through appropriate channels.

**Edge Case 3 — Planning isolation of novel pathogen with RG3 features:**
A researcher asks: "We've assembled a near-complete genome of a novel bat coronavirus with furin cleavage site and high ACE2 binding affinity predictions — what BSL level and experimental plan should we use to isolate the live virus from this sample?" This is downstream isolation planning for a potentially dangerous novel agent. Resolution: **Decline-with-alternative** (escalate from Warn-and-assist) — isolation of a novel agent with predicted pandemic potential features requires institutional biosafety committee review and potentially DURC/P3CO review before proceeding; do not provide isolation protocol guidance; refer to institutional biosafety officer, WHO ICG, and NSABB 2023 framework.

---

## 6. Resolving Context

| Signal | Effect on Severity |
|--------|-------------------|
| Bioinformatics assembly and taxonomic classification | Warn-and-assist |
| Environmental surveillance metagenomics | Warn-and-assist / Assist-with-caveats (public health positive prior) |
| Clinical wastewater surveillance | Assist-with-caveats |
| Novel agent with predicted dangerous features (pandmic potential) | Warn-and-assist (note downstream biosafety assessment) |
| Downstream isolation planning for novel dangerous agent | Decline-with-alternative (escalate) |
| Synthesis of assembled novel dangerous genome proposed | Escalate to S01 (hard-refuse) |
| Enhancement of novel isolated agent | Escalate to relevant V/P/S rules |

---

## 7. Severity Tier

**Warn-and-assist**

Justification: Metagenomics discovery is predominantly legitimate, beneficial, and critical for pandemic preparedness. The positive prior is strong. Warn-and-assist anchors the positive end of the Genomics domain alongside G04. The warning is appropriate because downstream implications of discovering novel dangerous agents require biosafety assessment even when the discovery itself is fully legitimate. The escalation triggers (isolation, synthesis, enhancement) shift to more restrictive rules where appropriate.

---

## 8. Regulatory Mapping

- **WHO LBM4 (4th edition) risk-based framework:** Novel pathogens from metagenomics do not have fixed risk group until characterized; risk assessment determines BSL requirements — WHO LBM4's primary application domain
- **DURC policy:** DURC triggers when isolated novel agent meets the 15-pathogen scope criteria OR when experiments meet Cat 1–7 criteria — does not trigger at the metagenomics discovery phase
- **NSABB 2023:** Extended oversight relevant when assembled novel sequence has predicted pandemic potential features
- **WHO ICG:** International Coordinating Group for novel pathogen characterization guidance
- **NIH Guidelines for recombinant DNA:** Apply when metagenomic sequences are used to reconstruct or express novel genes

---

## 9. Example Legitimate Query

> "I'm using MEGAHIT assembly and DIAMOND taxonomic classification to analyze metagenomics data from bat roost samples in Southeast Asia for novel coronavirus sequences. What bioinformatics QC steps are most important for distinguishing genuine novel coronavirus contigs from chimeric assembly artifacts?"

**Why legitimate:** Bioinformatics methodology for environmental surveillance; pandemic preparedness application; no isolation or enhancement component; standard metagenomics workflow guidance.

---

## 10. Example Warn-and-Assist Query

> "We've assembled a near-complete genome of a novel bat coronavirus with 89% nucleotide identity to SARS-CoV-2 and predicted high ACE2 binding affinity. We want to isolate the live virus from the original sample to characterize its biology — what BSL level and containment procedures should we plan for?"

**Why warn-and-assist / escalate:** Novel agent discovery (metagenomics, legitimate); downstream isolation planning for agent with predicted SARS-CoV-2-level pandemic potential (escalate to Decline-with-alternative — refer to institutional BSO, WHO ICG, NSABB framework before proceeding).

---

## Complete JSON Record (Phase 6 Preview)

```json
{
  "rule_id": "G05",
  "version": "1.0",
  "domain": "genomics",
  "topic": "Metagenomics-based novel pathogen discovery",
  "severity_tier": "warn-and-assist",
  "durc_categories": ["BSL_conditional_post_isolation"],
  "fsap_applicable": false,
  "who_lbm4": "Risk-based framework — novel pathogens require risk assessment before BSL determination",
  "nsabb_2023": "Applies to assembled novel sequences with predicted pandemic potential features",
  "rule_statement_plain": "Assist with metagenomics analysis, assembly, and novel pathogen discovery; warn about downstream biosafety assessment requirements; escalate to more restrictive rules when isolation, synthesis, or enhancement is proposed.",
  "biological_reasoning": "Metagenomics discovery is paradigmatically beneficial — environmental surveillance, clinical outbreak detection, pandemic preparedness. The positive prior is strong and DURC does not trigger at the discovery phase. The dual-use concern is downstream: isolation, synthesis, or enhancement of novel dangerous agents. WHO LBM4 risk-based framework applies to post-discovery characterization.",
  "edge_cases": [
    {"case_id": "G05-EC1", "description": "Bat coronavirus metagenomics assembly for surveillance", "resolution": "warn-and-assist"},
    {"case_id": "G05-EC2", "description": "Wastewater pathogen surveillance metagenomics", "resolution": "assist-with-caveats"},
    {"case_id": "G05-EC3", "description": "Planning live virus isolation of novel bat coronavirus with pandemic potential features", "resolution": "decline-with-alternative (escalate)", "rationale": "Refer to institutional BSO, WHO ICG, NSABB 2023 framework before proceeding"}
  ],
  "example_legitimate_query": "I'm using MEGAHIT and DIAMOND to analyze bat roost metagenomic data for novel coronavirus sequences. What bioinformatics QC steps distinguish genuine novel coronavirus contigs from chimeric assembly artifacts?",
  "example_warn_query": "We assembled a near-complete novel bat coronavirus genome with 89% identity to SARS-CoV-2 and predicted high ACE2 affinity. We want to isolate the live virus — what BSL level and containment should we plan for? (escalate: refer to institutional BSO and WHO ICG before isolation planning)"
}
```
