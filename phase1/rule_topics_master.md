# Phase 1: Rule Topics Master Table

> **Generated:** 2026-04-16
> **Purpose:** Definitive list of all 30 rule topics. Each row becomes one rule in Phase 3. This table is the primary input to Phase 3 (rule drafting) and Phase 2 (regulatory baseline extraction).

---

## Virology (Rules V01–V05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| V01 | Virology | Airborne transmission enhancement experiments | Hard-refuse | Cat 4 (transmissibility) | DURC Cat 4; FSAP Tier 1 (HPAI, 1918 flu); P3CO Framework (ePPP); Australia Group | The defining virology dual-use case (Fouchier/Kawaoka H5N1); no legitimate framing resolves enhancement of airborne transmissibility in dangerous pathogens |
| V02 | Virology | Host range alteration and cross-species experiments | Decline-with-alternative | Cat 5 (host range/tropism) | DURC Cat 5; FSAP (HPAI, select viruses); WHO RG classification | Wild-type characterization (legitimate) vs. engineered host range alteration (DURC) is the central ambiguity; institutional approval and P3CO status are the resolving context |
| V03 | Virology | Immune evasion mechanism characterization vs. engineering | Decline-with-alternative | Cat 2 (disrupt immunity) | DURC Cat 2; FSAP (select viral agents); WHO RG3–4 | Large legitimate base in vaccine research with a dangerous edge when framing shifts from understanding to engineering immune escape |
| V04 | Virology | Reconstruction/reconstitution of eradicated or extinct viruses | Hard-refuse | Cat 7 (reconstitute extinct agent) | DURC Cat 7; FSAP (variola, 1918 flu as select agents); Australia Group | Absolute prohibition: variola and 1918 flu reconstruction has no legitimate framing that resolves the risk; hard floor tested by two historically defined cases |
| V05 | Virology | Vaccine antigen design and standard virological characterization | Assist-with-caveats | None (not normally DURC) | FSAP vaccine exemptions; WHO RG2 baseline for most characterized viruses | Anchors the positive end; vaccine development and standard virological methods are explicitly encouraged uses; pathogen identity and enhancement framing are the few restricting variables |

---

## Toxicology (Rules T01–T05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| T01 | Toxicology | Mechanism of action of regulated toxins | Assist-with-caveats | None (mechanistic understanding, not enhancement) | FSAP (threshold applies to possession, not discussion); CWC Sched 1 (botulinum, ricin, saxitoxin); CWC Art. II.9(c) (protective research permitted) | Antidote development, cancer therapy (immunotoxins), and neuroscience require toxin mechanism understanding; this is primarily legitimate science that the rule must facilitate |
| T02 | Toxicology | Structure-activity relationships for lethality optimization | Hard-refuse | Cat 1 (enhance harmful consequences) | FSAP + CWC Sched 1; Australia Group | Potency optimization for listed toxins = weaponization with no legitimate framing; the hard floor for the toxicology domain |
| T03 | Toxicology | Production scale-up and quantity thresholds | Decline-with-alternative | Cat 1 (if enhancing production capability) | FSAP possession thresholds (>0.5 mg botulinum, >5 mg ricin, etc.); FSAP registration requirements | Threshold logic is the primary toxicology decision variable: quantity combined with stated purpose drives severity from assist to decline to refuse |
| T04 | Toxicology | Delivery mechanism and aerosol dispersal research | Hard-refuse | Cat 4 (dissemination); CWC Art. II (weaponization) | CWC Art. II definitions (chemical weapons include delivery means); FSAP; Australia Group (aerosol inhalation chambers) | Listed toxin identity + dispersal mechanism framing = weaponization signal with no legitimate defensive-research exception that resolves the concern in a query context |
| T05 | Toxicology | Antidote, countermeasure, and detection research | Assist-with-caveats | None (explicitly permitted) | FSAP exemptions; CWC Art. II.9(c) (protective purposes explicitly permitted); NIH/DARPA medical countermeasure programs | Explicitly permitted under international law; one of the largest legitimate biosafety research use cases; anchors the positive end of the toxicology domain |

---

## Synthetic Biology (Rules S01–S05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| S01 | Synthetic Biology | De novo DNA synthesis of select agent genome sequences | Hard-refuse | Cat 7 (reconstitute eradicated agent) | DURC Cat 7; IASB harmonized screening protocol (2022); FSAP (registration required for select agent equivalents); Australia Group | Full-genome synthesis of dangerous pathogens is the hard floor for this domain; IASB screening exists precisely to prevent this, and Claude's assistance in bypassing screening is categorically prohibited |
| S02 | Synthetic Biology | Genetic circuit design targeting pathogen characteristics | Decline-with-alternative | Cat 1–5 (context-dependent) | DURC Cat 1–5 (depends on circuit function); FSAP; iGEM biosafety policies | Common academic query at the iGEM-adjacent boundary; chassis organism identity (pathogen vs. E. coli) and modification type (virulence, toxin production, resistance) drive severity |
| S03 | Synthetic Biology | Directed evolution of virulence factors or toxin potency | Decline-with-alternative | Cat 1 (enhance harmful consequences) | DURC Cat 1; FSAP (if applied to select agents) | Directed evolution is a workaround for synthesis screening that Claude must recognize as functionally equivalent to de novo enhancement; wild-type baseline and selection pressure are the resolving context |
| S04 | Synthetic Biology | CRISPR editing of regulated pathogens | Decline-with-alternative | Cat 1, 2, 3 (depends on edit) | FSAP; BSL-3/4 requirements; institutional biosafety committee approval | CRISPR ubiquity makes this the most frequently queried synthetic biology topic; institutional BSL containment level and IBC-approved protocol are the primary resolving context |
| S05 | Synthetic Biology | Metabolic engineering and non-pathogen synthetic biology | Warn-and-assist | None (unregulated for non-pathogens) | Generally unregulated; Australia Group equipment controls if production scale is large | Anchors the positive end; biofuels, pharmaceutical metabolites, fermentation, and protein expression are overwhelmingly legitimate; organism identity (pathogen vs. not) is the primary axis |

---

## Genomics (Rules G01–G05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| G01 | Genomics | Functional annotation of select agent genomes | Decline-with-alternative | Cat 1–5 (depends on annotation target) | DURC Cat 1–5; NSABB 2023 sequence extension; NCBI access policies | NCBI/GISAID data access makes this very common; the ambiguity is published annotation (legitimate) vs. novel enhancement-predicting annotation (DURC) |
| G02 | Genomics | AI-assisted de novo design of novel dangerous pathogen sequences | Hard-refuse | Cat 7 principle (reconstitute/create novel equivalent) | DURC Cat 7 principle; IASB (downstream synthesis); emerging AI biosecurity frameworks | Fastest-growing dual-use risk: Claude is directly in the loop of AI-assisted sequence design; no resolving context justifies de novo design of novel sequences predicted to encode pandemic pathogens |
| G03 | Genomics | Pandemic potential prediction from viral sequence data | Decline-with-alternative | Cat 4, 5 (transmissibility, host range prediction) | NSABB 2023 sequence-based oversight extension; WHO ICG guidance; DURC Cat 4/5 | Sequence → pandemic potential prediction is the frontier dual-use in computational biology; the ambiguity is surveillance use (legitimate) vs. enhancement-guidance use |
| G04 | Genomics | Variant effect prediction for pathogen virulence determinants | Assist-with-caveats | Contextual (NSABB 2023 if applied to ePPP candidates) | NSABB 2023; WHO ICG; context-dependent DURC applicability | VEP is standard bioinformatics with an enormous legitimate base; virulence context elevates sensitivity but does not change the default; pathogen identity and downstream application are resolving context |
| G05 | Genomics | Metagenomics-based novel pathogen discovery | Warn-and-assist | BSL conditional (if novel pathogen isolated); DURC if isolated agent matches criteria | BSL risk assessment (WHO LBM4); DURC triggered only if resulting pathogen is isolated and meets criteria | Environmental surveillance and clinical metagenomics are predominantly legitimate; the positive prior is strong; downstream isolation and enhancement questions trigger escalation |

---

## Pathogen Biology (Rules P01–P05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| P01 | Pathogen Biology | Virulence factor characterization in regulated pathogens | Assist-with-caveats | None (characterization, not enhancement) | FSAP exemptions; WHO RG2–3 risk assessment; published literature baseline | The most over-refusal-prone topic: legitimate vaccine/drug target research vastly outnumbers dual-use research; the rule must explicitly protect this large legitimate base while flagging enhancement framing |
| P02 | Pathogen Biology | Virulence factor engineering for enhancement | Hard-refuse | Cat 1 (enhance harmful consequences) | DURC Cat 1; FSAP; WHO RG3/4 pathogen requirements | The hard floor for pathogen biology; the line between P01 (characterization) and P02 (enhancement) is the domain's central question, and this rule holds the restriction side |
| P03 | Pathogen Biology | Antibiotic/antiviral resistance engineering and deliberate transfer | Decline-with-alternative | Cat 3 (resistance to interventions) | DURC Cat 3; FSAP (if applied to select agents); WHO antimicrobial resistance framework | Common in clinical microbiology queries; discovery of natural resistance (legitimate) vs. deliberate engineering and transfer of resistance to pathogenic organisms (DURC Cat 3) |
| P04 | Pathogen Biology | Immune evasion mechanism studies in bacterial/fungal pathogens | Decline-with-alternative | Cat 2 (disrupt immunity) | DURC Cat 2; FSAP (if select agent); WHO RG3 requirements | Parallels V03 (virology) but for bacterial/fungal pathogens; understanding existing immune evasion is legitimate; engineering novel evasion is DURC |
| P05 | Pathogen Biology | Diagnostic biomarker and vaccine target identification | Assist-with-caveats | None (beneficial primary use) | FSAP exemptions (diagnostic and vaccine research); WHO global health priorities; NIH funding frameworks | Explicitly protected under FSAP exemptions and international health priorities; anchors the positive end; the primary legitimate use case for select agent research |

---

## Dual-Use Chemistry (Rules C01–C05)

| Rule ID | Domain | Topic Title | Severity Tier | Primary DURC Category | Regulatory Anchors | 1-Sentence Rationale |
|---------|--------|-------------|--------------|----------------------|-------------------|----------------------|
| C01 | Dual-Use Chemistry | CWC Schedule 1 compound synthesis and close structural analogs | Hard-refuse | N/A (CWC, not DURC) | CWC Art. II; CWC Schedule 1 list; Australia Group; OPCW verification regime | Treaty-prohibited synthesis with no legitimate framing that a query can provide; the absolute floor for the chemistry domain |
| C02 | Dual-Use Chemistry | Schedule 2/3 precursor acquisition and sourcing patterns | Decline-with-alternative | N/A (CWC) | CWC Schedules 2–3; Australia Group chemical precursor controls | The volume of dual-use chemistry concern lives here; precursor combinations + stated purpose + quantity drive severity; legitimate industrial/research purpose can resolve |
| C03 | Dual-Use Chemistry | AI-assisted molecular design targeting toxic bioactivity | Decline-with-alternative | N/A (CWC general purpose criterion) | CWC Art. II "general purpose criterion"; Urbina et al. (2022) empirical case | Claude is directly in the AI + chemistry loop; optimization target (therapeutic vs. toxic) and structural proximity to Schedule 1 determine severity |
| C04 | Dual-Use Chemistry | Delivery system and dispersal mechanism design for chemical agents | Hard-refuse | N/A (CWC Art. II covers delivery means) | CWC Art. II (weaponization definition includes delivery); Australia Group (aerosol equipment) | Delivery mechanism + chemical agent identity = weaponization signal; parallels T04 (toxin delivery) with the same logical structure |
| C05 | Dual-Use Chemistry | Reagent sourcing for routine biological research | Assist-with-caveats | None (unregulated standard lab practice) | Generally unregulated; BSL-relevant reagent restrictions if pathogen context present | Anchors the positive end; routine lab supply questions are legitimate biology; pathogen identity and BSL context — not the reagent itself — provide the few caveats |

---

## Summary Counts

| Domain | Hard-refuse | Decline-with-alternative | Assist-with-caveats | Warn-and-assist | Total |
|--------|------------|--------------------------|--------------------|-----------------|----|
| Virology | 2 (V01, V04) | 2 (V02, V03) | 1 (V05) | 0 | 5 |
| Toxicology | 2 (T02, T04) | 1 (T03) | 2 (T01, T05) | 0 | 5 |
| Synthetic Biology | 1 (S01) | 3 (S02, S03, S04) | 0 | 1 (S05) | 5 |
| Genomics | 1 (G02) | 2 (G01, G03) | 1 (G04) | 1 (G05) | 5 |
| Pathogen Biology | 1 (P02) | 2 (P03, P04) | 2 (P01, P05) | 0 | 5 |
| Dual-Use Chemistry | 2 (C01, C04) | 2 (C02, C03) | 1 (C05) | 0 | 5 |
| **Total** | **9** | **12** | **7** | **2** | **30** |
