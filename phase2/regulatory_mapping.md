# Phase 2: Regulatory Baseline Extraction

> **Generated:** 2026-04-16
> **Purpose:** Cross-reference all 30 rule topics to the 5 applicable regulatory frameworks. This file is the direct input to Phase 3 rule drafting — each regulatory mapping field (field 8 of the 10-field template) draws from this table.
> **Inputs:** `phase1/rule_topics_master.md`; `research/regulatory/*.md`

---

## Regulatory Framework Legend

| Abbreviation | Framework | Key Provision Types | Source File |
|---|---|---|---|
| **DURC** | NSABB USG Dual Use Research of Concern Policy (2013 + 2023 revisions) | 7 categories; 15 in-scope pathogens; ePPP definition | `research/regulatory/NSABB_DURC.md` |
| **FSAP** | Federal Select Agent Program (CDC HHS + USDA APHIS) | Tier 1 / Tier 2 lists; possession thresholds; registration exemptions | `research/regulatory/FSAP_SelectAgents.md` |
| **WHO-LBM4** | WHO Laboratory Biosafety Manual 4th Edition (2020) | Risk Groups RG1–4; BSL1–4; risk-based assessment | `research/regulatory/WHO_LBM4.md` |
| **BWC/CWC** | Biological Weapons Convention (Art. I) + Chemical Weapons Convention (Art. II + Schedules 1–3) | Treaty prohibitions; CWC purpose criterion; Schedule tiering | `research/regulatory/BWC_CWC.md` |
| **AG** | Australia Group Common Control Lists | Biological agents; human/animal pathogens; toxins; equipment; precursor chemicals | `research/regulatory/AustraliaGroup.md` |

---

## Master Cross-Reference Matrix

| Rule ID | Topic | DURC Cat | FSAP Status | WHO RG/BSL | BWC/CWC Provision | AG Lists |
|---------|-------|----------|-------------|------------|-------------------|----------|
| **VIROLOGY** | | | | | | |
| V01 | Airborne transmission enhancement | Cat 4 | T1 (1918 flu, HHS); USDA (HPAI H5/H7) | RG3–4; BSL-3 min | BWC Art I; P3CO ePPP framework | Biological agents; aerosol inhalation chambers |
| V02 | Host range alteration | Cat 5 | T1–2 (HPAI, select viruses); exemption: wild-type characterization | RG3–4 | BWC Art I | Biological agents; human/animal pathogens list |
| V03 | Immune evasion characterization vs. engineering | Cat 2 | T2 (select viral agents); exemption: vaccine design | RG3–4 | BWC Art I | Biological agents |
| V04 | Reconstruct eradicated/extinct viruses | Cat 7 | T1 (variola major, variola minor, 1918 flu — HHS) | RG4 (variola); BSL-4 | BWC Art I | Biological agents (variola, reconstructed 1918 flu) |
| V05 | Vaccine antigen design / standard characterization | None | FSAP vaccine exemption (if select agent antigen) | RG2 baseline (most characterized viruses) | Not applicable | Not applicable (routine work) |
| **TOXICOLOGY** | | | | | | |
| T01 | Mechanism of action, regulated toxins | None (mechanistic discussion, not possession) | Possession threshold rule (not discussion rule) | N/A (toxins not RG-classified) | CWC Sched 1 (botulinum, ricin, saxitoxin); Art II.9(c) permits protective research | AG toxins list (botulinum, ricin, abrin, saxitoxin, staphylococcal enterotoxins, conotoxins, others) |
| T02 | SAR for lethality optimization | Cat 1 | T1 (botulinum, ricin, abrin, saxitoxin, tetrodotoxin); threshold: >0.5–5 mg | N/A | CWC Sched 1 (potency optimization = weaponization) | AG toxins list |
| T03 | Production scale-up / quantity thresholds | Cat 1 (if scale = weaponization capacity) | FSAP possession thresholds (mg-level triggers): botulinum >0.5 mg, ricin >5 mg, abrin >0.5 mg, saxitoxin >5 mg | N/A | CWC quantity limits for Sched 1 (≤1 metric ton/yr aggregate) | AG equipment (fermenters ≥20 L; lyophilizers; spray dryers) |
| T04 | Delivery mechanism / aerosol dispersal | CWC Art II (delivery element of CW definition) | FSAP (listed toxins) | N/A | CWC Art II §1(a)(ii): "munitions and devices specifically designed to cause death or harm" | AG toxins; aerosol inhalation chambers; spray drying equipment |
| T05 | Antidote / countermeasure / detection | None (explicitly permitted) | FSAP diagnostic/therapeutic exemptions | N/A | CWC Art II.9(c): "protective purposes … development of … protection" explicitly permitted | Not applicable |
| **SYNTHETIC BIOLOGY** | | | | | | |
| S01 | De novo DNA synthesis of select agent genomes | Cat 7 | Registration equivalent (synthesis = possession equivalent if select agent) | RG of target organism | BWC Art I ("whatever their origin or method of production") | Biological agents (listed pathogens) |
| S02 | Genetic circuit design targeting pathogen characteristics | Cat 1–5 (function-dependent) | T1–2 if pathogen chassis; iGEM biosafety policy lower bound | RG of chassis organism | BWC Art I | Biological agents (if pathogen chassis) |
| S03 | Directed evolution of virulence/toxin potency | Cat 1 | FSAP (if select agent); directed evolution = enhancement regardless of method | RG3–4 (if select agent) | BWC Art I | Biological agents |
| S04 | CRISPR editing of regulated pathogens | Cat 1, 2, or 3 (edit-dependent) | FSAP; BSL-3/4 requirement; IBC approval | RG3–4 | BWC Art I | Biological agents |
| S05 | Metabolic engineering / non-pathogen synbio | None | Not applicable (non-pathogen) | RG1–2 (non-pathogen chassis) | Not applicable | AG equipment controls (fermenters ≥20 L at production scale) |
| **GENOMICS** | | | | | | |
| G01 | Functional annotation of select agent genomes | Cat 1–5 (annotation target-dependent) | FSAP (if applying novel functional prediction to select agent sequence) | RG3–4 | BWC Art I (if annotation guides enhancement) | Biological agents |
| G02 | AI-assisted de novo design of novel dangerous sequences | Cat 7 principle (de novo = reconstitution analog) | IASB downstream synthesis screening | RG3–4 (predicted) | BWC Art I ("whatever their … method of production") | Biological agents |
| G03 | Pandemic potential prediction from sequence | Cat 4, 5 | NSABB 2023 sequence-extension recommendation | RG3–4 | BWC Art I (if prediction guides enhancement) | Biological agents |
| G04 | Variant effect prediction for virulence determinants | Contextual (NSABB 2023 ePPP if applied to candidate pandemic pathogens) | FSAP (if applied to select agent sequence) | RG3–4 | BWC Art I (contextual) | Biological agents |
| G05 | Metagenomics-based novel pathogen discovery | BSL conditional (post-discovery if isolated) | Not FSAP at discovery stage; FSAP applies if isolated agent matches select agent criteria | WHO LBM4 risk assessment framework (not fixed RG until characterized) | BWC Art I (if enhancement follows) | Biological agents (if isolated and characterized) |
| **PATHOGEN BIOLOGY** | | | | | | |
| P01 | Virulence factor characterization in regulated pathogens | None (characterization without enhancement) | FSAP exemptions (diagnostic/vaccine research); published literature allowed | RG2–3 (characterization does not change BSL) | BWC Art I (not applicable: peaceful purpose) | Not applicable |
| P02 | Virulence factor engineering / enhancement | Cat 1 | FSAP (all Tier 1 + Tier 2 bacterial pathogens) | RG3–4 | BWC Art I | Biological agents |
| P03 | Antibiotic/antiviral resistance engineering / deliberate transfer | Cat 3 | FSAP (if applied to B. anthracis, Y. pestis, F. tularensis, B. mallei/pseudomallei) | RG3–4 | BWC Art I | Biological agents |
| P04 | Immune evasion mechanism studies (bacterial/fungal) | Cat 2 | FSAP (if select agent) | RG3–4 | BWC Art I | Biological agents |
| P05 | Diagnostic biomarker / vaccine target identification | None (beneficial primary use) | FSAP diagnostic and vaccine exemptions | RG2–3 (routine characterization) | Not prohibited under BWC | Not applicable |
| **DUAL-USE CHEMISTRY** | | | | | | |
| C01 | CWC Sched 1 synthesis / close structural analogs | N/A (CWC, not DURC) | Not FSAP (chemical agents, not biological) | N/A | CWC Sched 1 (direct listing); CWC Art II §2 (toxic chemicals); OPCW verification | AG precursor chemicals (alkyl phosphonyl difluorides, thiodiglycol, pinacolyl alcohol); chemical agents list |
| C02 | Schedule 2/3 precursor acquisition / sourcing | N/A (CWC) | Not FSAP | N/A | CWC Sched 2 (amiton, phosphorus trichloride, thiodiglycol, H₂CN); CWC Sched 3 (phosgene, cyanogen, HCN) | AG precursor chemicals list |
| C03 | AI-assisted molecular design for toxic bioactivity | N/A (CWC general purpose criterion) | Not FSAP | N/A | CWC Art II §2 general purpose criterion: any toxic chemical for hostile purposes, regardless of Schedule status | AG precursor chemicals |
| C04 | Delivery system / dispersal mechanism design | N/A (CWC Art II) | Not FSAP | N/A | CWC Art II §1(a)(ii): "munitions and devices specifically designed to cause death … through toxic chemicals"; Art II §1(a)(iii): "equipment specifically designed for use directly in connection" | AG: aerosol equipment; spray drying; cross-flow filtration (if for weaponization) |
| C05 | Reagent sourcing for routine biological research | N/A | N/A | N/A | Not applicable | Not applicable (routine reagents uncontrolled) |

---

## Per-Domain Regulatory Notes

### Domain 1 — Virology

**Primary regulatory anchors:** DURC Categories 4, 5, 7; FSAP Tier 1 (variola, 1918 flu, HPAI); P3CO Framework; Australia Group biological agents and equipment lists.

- **FSAP Tier 1 in virology:** Reconstructed 1918 influenza, variola major, variola minor — these three viruses carry the highest regulatory burden. SARS-CoV (original) is HHS listed; SARS-CoV-2 was not a select agent as of August 2025.
- **HPAI regulatory split:** Highly pathogenic avian influenza (H5, H7) is a USDA select agent, not HHS — a distinction relevant to jurisdiction for rule mapping.
- **P3CO Framework:** Research qualifying as ePPP research (creating an enhanced potential pandemic pathogen) requires HHS P3CO review. Rules V01 and V02 touch this framework most directly. P3CO review does not authorize Claude assistance — it authorizes the research, not the AI layer.
- **V05 exemption:** Standard vaccine antigen design for non-enhancement purposes is explicitly exempted from FSAP and does not constitute DURC. WHO RG2 is the baseline risk group for most well-characterized non-select viruses used in vaccine development.
- **Cross-regulatory overlap:** Several RG4 pathogens (Ebola, Marburg, variola, Nipah) appear on FSAP Tier 1 or Tier 2, Australia Group biological agents list, and WHO RG4 simultaneously. Triple-listed = highest severity signal.

---

### Domain 2 — Toxicology

**Primary regulatory anchors:** FSAP Tier 1 toxins (botulinum, ricin, abrin, saxitoxin, conotoxins, tetrodotoxin); CWC Schedule 1 (botulinum, ricin, saxitoxin overlap); Australia Group toxin list (broader than CWC Sched 1); CWC Art. II.9(c) (protective research explicitly permitted).

- **Double-listed toxins:** Botulinum neurotoxins, ricin, and saxitoxin appear on both FSAP Tier 1 and CWC Schedule 1. This double listing creates the highest severity anchor for T02 and T04.
- **AG toxin list broader than CWC Sched 1:** Australia Group controls abrin, aflatoxins, DAS, HT-2 toxin, staphylococcal enterotoxins — these are not CWC-scheduled but are internationally export-controlled. Rules must cite both authorities where applicable.
- **Threshold principle:** FSAP possession thresholds (mg-level) create a regulatory step function: below threshold = unregulated possession, above threshold = registration required. T03 encodes this step function as severity logic.
- **CWC Art. II.9(c) protective research permission:** This explicit treaty carve-out is the regulatory anchor for T05 (antidote/countermeasure/detection). The rule should mirror the treaty language: "protective purposes, including research into, and development of, methods of protection against … toxic chemicals."
- **Aerosol equipment:** Australia Group controls aerosol inhalation chambers and spray drying equipment — relevant to T04 (delivery mechanism queries) where equipment + toxin combination is the dual-use signal.

---

### Domain 3 — Synthetic Biology

**Primary regulatory anchors:** DURC Category 7 (reconstitution); IASB Harmonized Synthesis Screening Protocol (2022); FSAP registration (synthesis equivalent to possession); Australia Group equipment controls at production scale.

- **IASB Screening Protocol:** The International Alliance for Biological Standardization's harmonized DNA synthesis screening guidelines (2022) cover genome-length sequences matching FSAP select agents. S01 maps directly to this framework as the primary operational mechanism.
- **BWC "whatever their origin or method of production":** This clause in BWC Art. I explicitly covers synthetic biology routes — the treaty's drafters anticipated novel production methods. S01 through S04 all draw on this provision.
- **DURC by proxy for synthetic biology:** Synthetic biology experiments that achieve DURC-qualifying outcomes in non-listed organisms may still trigger institutional DURC review if the outcome itself (e.g., enhanced toxin production, airborne transmissibility) meets Cat 1–7 criteria.
- **iGEM biosafety policies:** iGEM's biosafety review provides a useful lower-bound calibration — work accepted by iGEM biosafety review is baseline acceptable; work refused by iGEM represents minimal-context dual-use.
- **S05 Australia Group equipment caveat:** Large-scale fermenters (≥20 L working volume) are Australia Group-controlled even for non-pathogen metabolic engineering. Queries about production-scale fermentation with listed organisms require export context review.

---

### Domain 4 — Genomics

**Primary regulatory anchors:** NSABB 2023 sequence-extension recommendations; IASB downstream synthesis controls; WHO LBM4 risk assessment framework (for metagenomics); DURC Categories 4 and 5 (transmissibility and host range prediction from sequence).

- **NSABB 2023 is the key evolving anchor:** The 2023 NSABB recommendations explicitly extended oversight to *sequence-based* prediction of pandemic potential — even without wet lab synthesis. This makes G01, G02, G03 more regulated than the pre-2023 framework anticipated.
- **AI governance gap:** No current U.S. regulation specifically governs AI-assisted biological sequence design (G02). Rule G02 is grounded in BWC Art. I principles and IASB downstream controls — the closest applicable anchors. This regulatory gap is itself a novelty note for the library.
- **NCBI/GISAID controlled access:** Some select agent sequences have controlled database access — relevant context for G01 (annotation) and G02 (de novo design that closely matches controlled sequences).
- **Metagenomics regulatory trigger:** G05 is outside DURC scope at the discovery stage (before isolation). The regulatory anchor shifts to WHO LBM4 risk assessment once a novel agent is isolated and characterized — a downstream trigger rather than an upfront prohibition.

---

### Domain 5 — Pathogen Biology

**Primary regulatory anchors:** DURC Categories 1, 2, 3; FSAP (bacterial Tier 1: B. anthracis, F. tularensis, Y. pestis; Tier 2: Brucella, B. mallei/pseudomallei, C. burnetii, R. prowazekii); WHO RG3 (most controlled bacteria); FSAP diagnostic and vaccine exemptions.

- **Characterization vs. enhancement asymmetry (P01 vs. P02):** The DURC framework explicitly does not prohibit virulence factor *characterization* — only enhancement. This P01/P02 boundary is the central regulatory finding for the domain and must be clearly drawn in rules.
- **FSAP exemptions for diagnostics and vaccines:** The FSAP explicitly exempts diagnostic activities and vaccine development from certain registration requirements. P01 (virulence factor characterization for vaccine targets) and P05 (diagnostic biomarkers) draw on these exemptions.
- **WHO AMR framework:** WHO's Global Action Plan on Antimicrobial Resistance (2015) establishes antimicrobial resistance research as a global health priority. P03's regulatory mapping must distinguish between AMR discovery research (legitimate, WHO-priority) and deliberate AMR engineering in select agent hosts (DURC Cat 3).
- **Bacterial RG3 group:** B. anthracis, Y. pestis, F. tularensis, B. mallei, B. pseudomallei, C. burnetii are all WHO RG3 and FSAP-listed. This cluster defines the high-sensitivity space for P01–P04.

---

### Domain 6 — Dual-Use Chemistry

**Primary regulatory anchors:** CWC Schedules 1–3; CWC Art. II (general purpose criterion and weaponization definition); Australia Group chemical precursors list.

- **DURC non-applicability:** DURC policy covers *biological* research. All C01–C05 rules use CWC and Australia Group as primary anchors. DURC column is N/A for the entire chemistry domain.
- **CWC General Purpose Criterion:** CWC Art. II prohibits *any* toxic chemical developed, produced, or stockpiled for hostile purposes, regardless of Schedule status. This "catch-all" provision anchors C03 (AI-assisted molecular design targeting toxicity) where the compound may not be Schedule-listed.
- **Schedule tiering maps to severity tiering:** CWC Sched 1 → Hard-refuse (C01, C04); Sched 2–3 → Decline-with-alternative (C02); general purpose criterion → Decline-with-alternative (C03); below-schedule routine reagents → Assist-with-caveats (C05). The CWC's own tiering aligns with the severity tier structure.
- **CWC delivery means:** CWC Art. II §1(a)(iii) explicitly includes "equipment specifically designed for use directly in connection with" chemical weapons munitions — grounding C04 (delivery system design) as a hard-refuse topic.
- **Australia Group precursor chemicals:** Controls include nerve agent precursors (alkyl phosphonyl difluorides, O-alkyl dialkylphosphoramidothioates) and mustard precursors (thiodiglycol, pinacolyl alcohol). These are export-controlled even before synthesis of the final CW agent — relevant to C02 and C03.

---

## Key Cross-Domain Regulatory Observations

**1. FSAP Tier 1 + CWC Sched 1 double-listing = Hard-refuse floor in multiple domains.**
Botulinum toxin, ricin, saxitoxin: listed on FSAP Tier 1 AND CWC Schedule 1. Ebola, Marburg, variola: FSAP Tier 1 AND WHO RG4. Double-listed entities generate the highest regulatory burden and anchor the Hard-refuse tier consistently across Virology and Toxicology domains.

**2. Delivery mechanism = universal Hard-refuse trigger.**
T04 (toxicology) and C04 (chemistry) both reach Hard-refuse because CWC Art. II's definition of chemical weapons explicitly includes delivery means. V01's airborne enhancement is a variant of this principle — transmissibility engineering = biological delivery optimization. The rule structure reflects this shared logic.

**3. Protective/countermeasure research = universal Assist trigger.**
CWC Art. II.9(c) and FSAP diagnostic/vaccine exemptions create consistent positive-end rules: T05 (antidote research), P05 (vaccine targets), V05 (vaccine antigen design) all draw on equivalent regulatory carve-outs. The Assist-with-caveats tier is the right calibration for these topics.

**4. NSABB 2023 creates a computational biology extension that post-dates most prior classifier training.**
G01, G02, G03 are now subject to oversight recommendations that did not exist before 2023. Classifiers trained before 2023 may systematically under-restrict computational genomics queries targeting pandemic potential. This library explicitly encodes the post-2023 regulatory baseline.

**5. Australia Group toxin list is materially broader than CWC Schedule 1.**
CWC Sched 1 controls botulinum, ricin, saxitoxin (among biological toxins). Australia Group adds abrin, aflatoxins, DAS, HT-2 toxin, staphylococcal enterotoxins, shiga toxin, conotoxins, tetrodotoxin, viscumin. T02 and T03 must cite both lists to achieve full regulatory coverage.

**6. BWC Art I's "whatever their origin or method of production" covers all synthetic biology routes.**
This clause was prescient: it explicitly extends to synthetic biology, directed evolution, and AI-assisted design. S01, S03, G02 all draw on this provision as the foundational treaty anchor for non-natural production routes to dangerous biological agents.
