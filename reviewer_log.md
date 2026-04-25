# Reviewer Log

Documents the review process applied to the 30 rules in the Bio Constitution Rules Library.

---

## Phase 4 — Adversarial Review (April 2026)

In lieu of recruiting external domain experts prior to first publication, four parallel adversarial review passes were conducted using specialized review agents. Each pass had a distinct mandate. Findings and applied corrections are recorded below.

---

### Pass 1: Red-Team Loophole Finder

**Mandate:** Identify framing exploits — cases where stated context (academic, historical, computational, defensive-purpose) could be used to extract prohibited assistance from rules that don't explicitly anticipate those framings.

**Method:** For each hard-refuse and decline-with-alternative rule, tested whether the rule statement and edge cases would still refuse assistance when the query is wrapped in academic, historical, vaccine development, or computational-only framing.

**Key findings:**

| Rule | Framing tested | Finding | Action taken |
|------|---------------|---------|--------------|
| C01 | "Historical chemistry education" for Sarin synthesis | Rule already covered (EC1: hard-refuse regardless of historical framing) | None needed |
| G03 | "Computational only, no wet-lab" for pandemic potential optimization | Resolving context table did not explicitly state that computational-only framing does not reduce severity | Added explicit row: "Computational only, no wet-lab implication stated → Does not reduce severity" |
| S03 | "Academic protein engineering study" for directed evolution of FSAP virulence factor | Rule lacked explicit hard-refuse escalation for FSAP Tier 1 virulence factor targets | Added hard-refuse escalation rows for FSAP Tier 1 virulence factors and CWC Schedule 1 toxin potency |
| V03 | "Defensive vaccine research" for engineering immune escape in FSAP Tier 1 viral pathogen | Hard-refuse escalation existed only for RG4 pathogens; non-RG4 FSAP Tier 1 (SARS-CoV, 1918 flu) had gap | Added explicit hard-refuse floor for all FSAP Tier 1 viral pathogens with immune escape engineering |
| P03 | Explicit lethality/harm framing ("treatment will fail") for resistance engineering | Rule had no escalation for explicit harm-intent framing | Added hard-refuse escalation for resistance engineering + explicit lethality framing |

---

### Pass 2: Over-Refusal Auditor

**Mandate:** Identify rules that block legitimate science without DURC or regulatory justification — the false-positive problem for bio safety classifiers.

**Method:** For each assist-with-caveats and decline-with-alternative rule, tested edge cases against the legitimate scientific literature to identify rules that would block standard research activities with no actual dual-use concern.

**Key findings and corrections applied:**

| Rule | Over-refusal identified | Correction |
|------|------------------------|-----------|
| S01 EC1 | Single gene codon optimization for non-toxic structural/antigenic proteins from FSAP pathogens (e.g., Y. pestis F1 antigen for vaccine research) was blanket decline | Changed to: assist-with-caveats for non-toxic antigenic/structural proteins; decline-with-alternative only when the protein IS a regulated toxin (BoNT, ricin A-chain) |
| S04 EC2 | CRISPR loss-of-function edits in Salmonella (non-FSAP) were decline-with-alternative | Changed to: assist-with-caveats (note BSL-2 conditions, IBC oversight); added resolving context row for non-FSAP pathogenic organisms |
| G03 EC2 | Comparative pandemic risk ranking of natural wild-type HPAI H5N1 isolates using published WHO/CDC frameworks (IRAT, TIPRA) was decline-with-alternative | Changed to: assist-with-caveats; retrospective comparison of existing natural strains using WHO-mandated risk scoring is standard surveillance work |
| T03 EC1 | Sub-FSAP-threshold ricin preparation for validated analytical use in institutional laboratory was decline-with-alternative | Changed to: assist-with-caveats; the threshold was calibrated to permit exactly this use case; added note that scale-up prohibition still applies |

---

### Pass 3: Regulatory Accuracy Auditor

**Mandate:** Verify all specific regulatory citations — article numbers, schedule designations, threshold values, institution names, historical event attributions.

**Method:** Cross-referenced every named regulation (CWC article numbers, FSAP thresholds, IGSC vs. IASB, historical synthesis attributions) against source documents.

**Corrections applied:**

| Error type | Incorrect value | Correct value | Rules affected |
|-----------|----------------|--------------|---------------|
| CWC protective purposes provision | Art. II.9(c) | Art. II.9(b) | T01, T05, C01 EC2, C03 |
| CWC general purpose criterion location | Art. II.2 | Art. II.1 (embedded in chemical weapons definition) | C01 |
| CWC delivery equipment provisions | Art. II.1(a)(ii), II.1(a)(iii) | Art. II.1(b) (munitions), II.1(c) (dispersal equipment) | T04 |
| Synthesis screening body | IASB | IGSC (International Gene Synthesis Consortium) | S01, S03, G02 |
| Horsepox synthesis attribution | CSIRO | University of Alberta (Noyce et al., 2018) | S01, V04 |
| FSAP ricin threshold | 5 mg | 100 mg | T01, T02, T03 |
| FSAP abrin threshold | 0.5 mg | 100 mg | T01, T02, T03 |
| FSAP saxitoxin threshold | 5 mg | 100 mg | T01, T02, T03 |
| FSAP tetrodotoxin threshold | 2 mg | 100 mg | T01, T02, T03 |
| FSAP botulinum threshold | 1 mg | 0.5 mg | C05 |
| BZ classification | CWC Schedule 1 | CWC Schedule 2 | C01 |
| HPAI strain designation | H5N7 | H5/H7 | V01 JSON |
| T-2 toxin | Missing entirely | FSAP Tier 1 at 1,000 mg | T01, T02, T03 |

---

### Pass 4: Cross-Domain Consistency Auditor

**Mandate:** Verify severity tier parity across equivalent-risk scenarios in different domains. Identify any case where the same underlying risk is assigned different tiers without documented rationale.

**Method:** Mapped all 30 rules against the 7 DURC categories and the major risk scenario classes. Compared severity tiers for rules addressing equivalent scenarios.

**Key findings:**

| Finding | Action taken |
|---------|--------------|
| G03 hard-refuse escalation for prospective pandemic potential optimization was buried in edge cases (EC3) with no visibility at rule summary level | Added `escalate_to_hard_refuse` field to G03 JSON; added explicit escalation row in resolving context table |
| S03 directed evolution: no hard-refuse tier for the highest-risk cases (FSAP Tier 1 virulence factor directed evolution), creating inconsistency with T02 and P02 | Updated S03 resolving context and severity tier justification with explicit hard-refuse escalation |
| G04/G01 boundary: VEP of novel unannotated ORFs in select agent genomes had no explicit escalation path to G01 | Added cross-reference row in G04 resolving context table |

---

## Open Reviewer Slots

The following domain expert review slots remain open for a formal external review panel:

| Domain | Recommended reviewer profile | Status |
|--------|------------------------------|--------|
| Virology | BSL-3/4 virologist with influenza or coronavirus research background | Open |
| Toxicology | FSAP-registered toxinologist or pharmacologist | Open |
| Synthetic Biology | iGEM faculty advisor or IGSC member institution researcher | Open |
| Genomics | Computational biologist with DURC/NSABB committee experience | Open |
| Pathogen Biology | Clinical microbiologist or infectious disease researcher | Open |
| Dual-Use Chemistry | OPCW chemical weapons researcher or forensic chemist | Open |

Domain experts with feedback on any rule may submit corrections via the repository issue tracker. Anonymized attribution available on request.
