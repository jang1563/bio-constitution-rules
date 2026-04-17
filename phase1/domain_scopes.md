# Phase 1: Domain Scope Notes

> **Generated:** 2026-04-16
> **Purpose:** Design contract for Phase 3 (rule drafting). Locks domain boundaries, inclusion/exclusion criteria, and regulatory anchors. Must be finalized before rule drafting begins.

---

### Domain 1: Virology

**One-sentence definition:** Virology covers questions about the biology, characterization, engineering, and experimental manipulation of viruses, including transmission, host range, immune evasion, pathogenesis, and vaccine/antiviral development.

**Inclusion (in scope for rules):**
- Experimental enhancement of viral transmissibility, aerosol stability, or dissemination capacity
- Host range alteration experiments: adapting viruses to new host species or tissues
- Immune evasion mechanism research with enhancement framing (modifying NS1, VP35, ORF3a, or analogous interferon antagonists)
- Reconstruction or reconstitution of eradicated or extinct viruses from sequence data or archived material
- Chimeric virus construction combining elements from multiple virus strains or species
- Questions about mutation signatures associated with increased pandemic potential in influenza, coronaviruses, or other ePPP candidates
- Vaccine antigen design for select agent viruses and standard virological characterization methods

**Exclusion (out of scope — handled by other domains or unregulated):**
- Bacterial, fungal, or parasitic pathogen biology → handled by Pathogen Biology (Domain 5)
- DNA synthesis of viral genomes → handled by Synthetic Biology (Domain 3)
- Sequence-level computational analysis of viral virulence → primarily handled by Genomics (Domain 4), with overlap
- Standard clinical virology (TCID50, plaque assay, serology) for non-select agents without enhancement context → no rule needed (default: assist)
- Vaccine immunology and clinical trial design → unregulated

**Primary legitimate use base:** Vaccine development, antiviral drug discovery, outbreak surveillance, and fundamental virology account for the vast majority of virology questions; the legitimate scientific base is enormous, and rules must allow this while flagging enhancement contexts.

**Boundary with adjacent domains:**
- **Pathogen Biology:** Virology = viral pathogens only; Pathogen Biology = bacterial/fungal/parasitic virulence, plus host-pathogen interaction at the systems level
- **Genomics:** Virology handles wet-lab experimental questions; Genomics handles computational sequence analysis and AI-assisted design
- **Synthetic Biology:** Virology handles phenotypic characterization; Synthetic Biology handles de novo synthesis and genetic circuit design

**Key regulatory anchors for this domain:**
- DURC Categories 2, 4, 5, 7 (immune evasion, transmissibility, host range, reconstitution)
- FSAP Tier 1 select agents: Ebola, Marburg, 1918 flu, smallpox, Y. pestis (viral portion)
- WHO Risk Groups 3–4: filoviruses, variola, SARS-CoV
- HHS P3CO Framework: ePPP-creating research (GOF with pandemic potential)
- Australia Group: hemorrhagic fever viruses, HPAI, reconstructed 1918 flu

**Scope note:** Virology is the highest-sensitivity domain for dual-use concern because pandemic-capable pathogens are biological weapons by nature of their transmissibility. The 2011–2012 H5N1 controversy established the modern governance framework: experiments that could yield transmissible variants of dangerous viruses require special oversight regardless of scientific intent. This domain's rules address the spectrum from the hardest cases (reconstitution of extinct viruses, airborne transmission enhancement — where no legitimate framing resolves the concern) through mid-range ambiguities (host range studies, chimeric viruses — where institutional context and P3CO review status matter) to positive use cases (vaccine antigen design, standard virological characterization — where pathogen identity and enhancement framing are the resolving variables). The domain excludes bacterial and fungal pathogens, which belong to Pathogen Biology, and defers sequence-level computational analysis to Genomics.

---

### Domain 2: Toxicology

**One-sentence definition:** Toxicology covers questions about the biology, chemistry, mechanism, production, and delivery of regulated biological toxins and toxin analogs, spanning antidote development at one end and weaponization research at the other.

**Inclusion (in scope for rules):**
- Mechanism of action questions for FSAP-listed or CWC Schedule 1 toxins (botulinum, ricin, abrin, saxitoxin, SEB, etc.)
- Structure-activity relationship questions targeting lethality, potency, or receptor affinity optimization
- Production quantity and scale-up questions that approach or exceed FSAP possession thresholds
- Delivery mechanism research: aerosolization, particle size optimization, dispersal modeling for listed toxins
- Novel toxin synthesis or structural analog design with unknown but potentially high toxicity
- Antidote, medical countermeasure, and detection method research for regulated toxins
- Immunotoxin and antibody-drug conjugate research involving regulated toxin warheads

**Exclusion (out of scope — handled by other domains or unregulated):**
- CWC Schedule 1 organophosphate (nerve agent) synthesis → handled by Dual-Use Chemistry (Domain 6)
- Toxin gene synthesis or genetic circuit encoding toxin production → handled by Synthetic Biology (Domain 3)
- Environmental toxin monitoring (saxitoxin in shellfish, ciguatoxin in fish) at sub-threshold research scale → unregulated standard ecology
- Below-threshold academic toxicology (LD50 data in published papers, mechanism review articles) → no rule needed (default: assist)
- Drug discovery with toxin-derived pharmacophores at therapeutic scale → unregulated pharmaceutical development

**Primary legitimate use base:** Antidote development, medical countermeasures, diagnostics, neuroscience (botulinum A in tremor/spasticity treatment), and cancer therapy (immunotoxins, ADCs) constitute the overwhelming legitimate use base; toxin rules must facilitate this while flagging potency-optimization and delivery contexts.

**Boundary with adjacent domains:**
- **Dual-Use Chemistry:** Toxicology = protein/peptide biological toxins; Dual-Use Chemistry = synthetic organophosphates, CWC-scheduled small molecules, precursor chemicals
- **Synthetic Biology:** Toxicology = the toxin molecule itself; Synthetic Biology = the genetic constructs producing or encoding toxins
- **Pathogen Biology:** Toxicology = secreted/isolated toxin molecules; Pathogen Biology = the toxin-producing organism's virulence

**Key regulatory anchors for this domain:**
- FSAP: Botulinum neurotoxins (>0.5 mg), ricin (>5 mg), abrin (>0.5 mg), SEB, saxitoxin (>5 mg), conotoxins, DAS, T-2 toxin
- CWC Schedule 1: botulinum toxin, ricin, saxitoxin (also scheduled)
- Australia Group: full biological toxin control list
- CWC Art. II.9(c): explicitly permits protective/detection research on Schedule 1 agents

**Scope note:** Biological toxins occupy a unique dual-use position: the same molecule that is a Tier 1 bioterrorism threat (botulinum neurotoxin as a bioweapon) is also a therapeutic approved in multiple indications (onabotulinumtoxinA/Botox). Ricin is a potential weapon and a research tool in targeted cancer therapy. This paradox structures the domain's rules: the primary decision variables are not the toxin identity alone, but the combination of (quantity relative to FSAP threshold) × (question type: mechanism vs. potency-optimization vs. delivery vs. countermeasure). Rules must facilitate the large legitimate science base — antidote development, immunotoxin oncology, neurotoxin mechanistic research — while hard-refusing the specific combinations that constitute weaponization: potency optimization, above-threshold production scale-up, and dispersal mechanism design. The domain explicitly excludes CWC Schedule 1 synthetic chemical weapons (nerve agents), which belong to Dual-Use Chemistry, and genetic constructs encoding toxins, which belong to Synthetic Biology.

---

### Domain 3: Synthetic Biology

**One-sentence definition:** Synthetic Biology covers questions about the design, construction, and engineering of biological systems — including de novo DNA synthesis, genetic circuit design, directed evolution, CRISPR editing of pathogens, and metabolic engineering — with a focus on the engineering layer that transforms sequence information into functional organisms or parts.

**Inclusion (in scope for rules):**
- De novo synthesis of DNA sequences encoding regulated pathogen genomes or significant portions thereof
- Requests to circumvent, bypass, or evaluate DNA synthesis screening systems (IASB guidelines)
- Genetic circuit design targeting virulence, pathogenicity, or toxin production characteristics in pathogen chassis
- Directed evolution of virulence factors, toxin potency, or antibiotic resistance in regulated organisms
- CRISPR and other site-specific editing of select agents or BSL-3/4-classified pathogens
- Gene drive design and ecological release planning
- Reconstitution workflows combining synthetic DNA fragments into functional pathogen equivalents
- Metabolic engineering of non-pathogen organisms for industrial or pharmaceutical applications (positive end)

**Exclusion (out of scope — handled by other domains or unregulated):**
- Phenotypic characterization of existing viruses without engineering → Virology (Domain 1)
- Bioinformatic analysis of pathogen sequences without synthesis or engineering → Genomics (Domain 4)
- Toxin molecule mechanism and delivery → Toxicology (Domain 2)
- Standard molecular biology techniques (PCR, cloning, transformation) without pathogen/dangerous context → unregulated
- Protein expression and purification of non-dangerous proteins → unregulated

**Primary legitimate use base:** Metabolic engineering for pharmaceuticals (insulin, antibiotics, immunologics), biofuels, agricultural biotechnology, cell-free systems for diagnostics, and protein engineering for therapeutics constitute the enormous legitimate use base; organism identity (pathogen vs. not) is the primary axis that separates legitimate from concerning.

**Boundary with adjacent domains:**
- **Virology:** Synthetic Biology handles the construction and engineering step; Virology handles the phenotypic characterization of the resulting virus
- **Genomics:** Synthetic Biology handles the design-build-test cycle; Genomics handles the sequence analysis and computational prediction upstream of synthesis
- **Pathogen Biology:** Synthetic Biology handles the engineering of new properties; Pathogen Biology handles the study of existing natural properties

**Key regulatory anchors for this domain:**
- DURC Categories 4, 7 (transmissibility enhancement, reconstitution of eradicated agents)
- IASB harmonized DNA synthesis screening protocol (2022)
- FSAP: registration required for synthesis yielding select agents or their functional equivalents
- Australia Group: fermenters, spray dryers, aerosol chambers (equipment controls for large-scale production)
- CBD Cartagena Protocol: gene drives and environmental release of engineered organisms

**Scope note:** Synthetic biology is the domain with the most rapidly changing risk profile, driven by declining DNA synthesis costs, CRISPR democratization, and AI-assisted sequence design. The dual-use concern spans the full design-build-test cycle: AI-generated sequences (Genomics domain boundary), ordered DNA synthesis (IASB screening), genetic circuit assembly (this domain), and organism characterization (Virology/Pathogen Biology boundary). Rules in this domain focus on the engineering layer: the construction of functional biological entities from sequence parts. The hardest cases are de novo synthesis of select agent genomes (no legitimate use justification) and synthesis screening bypass (no legitimate use justification); mid-range cases include CRISPR editing of regulated pathogens (institutional approval and BSL containment are resolving context) and directed evolution of virulence factors (wild-type baseline and selection pressure matter); the positive end anchors on metabolic engineering of non-pathogen organisms, where organism identity is the primary differentiator. DNA synthesis screening exists precisely for this domain — rules should align with and reinforce the IASB framework.

---

### Domain 4: Genomics

**One-sentence definition:** Genomics covers questions about biological sequence analysis, variant effect prediction, AI-assisted sequence design, and metagenomics — specifically where computational analysis of nucleic acid or protein sequences has dual-use implications through its potential to enable pathogen enhancement, pandemic potential prediction, or novel dangerous organism design.

**Inclusion (in scope for rules):**
- Functional annotation of select agent or regulated pathogen genomes aimed at identifying or predicting enhanced virulence
- AI-assisted de novo design of novel nucleic acid or protein sequences with predicted dangerous biological activity
- Computational prediction of pandemic potential, transmissibility, or host range from viral sequence data
- Variant effect prediction (VEP) for known virulence determinants in regulated pathogens (e.g., predicting which HA mutations confer transmissibility)
- Metagenomics-based discovery, assembly, and characterization of novel pathogens in environmental or clinical samples
- Genomic sequence database queries that seek synthesis or reconstruction guidance for regulated pathogens

**Exclusion (out of scope — handled by other domains or unregulated):**
- Wet-lab experimental manipulation of pathogen sequences → Synthetic Biology (Domain 3) and Virology (Domain 1)
- Standard clinical sequencing and diagnostic genomics → unregulated (no rule needed, default: assist)
- Human population genetics, GWAS, ancestry inference for disease susceptibility → unregulated
- Standard bioinformatics methods (BLAST, MSA, phylogeny) applied to non-pathogen sequences → unregulated
- Variant effect prediction for human genetic variants (ClinVar, gnomAD) → unregulated
- Metagenomic taxonomy and diversity analysis without pathogen identification → unregulated

**Primary legitimate use base:** Outbreak surveillance, clinical diagnostics, pandemic preparedness, phylogenetic epidemiology, vaccine antigen design, and drug target identification constitute the overwhelming legitimate use base; the primary dual-use risk is a subset of these applications where the analytical output directly enables pathogen enhancement or construction.

**Boundary with adjacent domains:**
- **Synthetic Biology:** Genomics = sequence analysis and design; Synthetic Biology = physical construction from sequence
- **Virology:** Genomics = computational/in silico analysis; Virology = wet-lab experimental characterization
- **Pathogen Biology:** Genomics = sequence-level functional prediction; Pathogen Biology = experimental characterization of protein function

**Key regulatory anchors for this domain:**
- NSABB 2023 recommendations: extended oversight to sequence-based pandemic potential prediction
- DURC Category 5 (host range alteration) — applicable when sequence analysis directly guides host range experiments
- IASB DNA synthesis screening: downstream anchor (sequence design feeds synthesis)
- WHO ICG guidance on pandemic potential prediction

**Scope note:** Genomics is the domain with the most frontier dual-use risk, driven by the convergence of large sequence databases, AI-powered functional prediction, and declining synthesis costs. The central dual-use concern is sequence-to-function: as computational tools become better at predicting what sequences do, the gap between "analyzing a sequence" and "enabling its construction or enhancement" narrows. The 2023 NSABB recommendations explicitly extended oversight to sequence-based pandemic potential prediction, acknowledging that wet-lab experiments are no longer the sole DURC concern. This domain's rules address: the hard case of AI-assisted design of novel dangerous sequences (no resolving context); mid-range cases of functional annotation and pandemic potential prediction (surveillance context, pathogen identity, and downstream application are resolving variables); and positive cases like VEP for published pathogen sequences and environmental metagenomics (where the legitimate-use prior is strong and the downstream enhancement pathway is indirect). The domain explicitly excludes wet-lab operations, which belong to Synthetic Biology and Virology, and standard human/non-pathogen genomics, which is unregulated.

---

### Domain 5: Pathogen Biology

**One-sentence definition:** Pathogen Biology covers questions about the mechanistic biology of bacterial, fungal, and parasitic pathogens — including virulence factor characterization, host-pathogen interaction, immune evasion, antibiotic resistance, and diagnostic/vaccine target identification — with the central dual-use tension between studying what pathogens do naturally (legitimate) and engineering them to do it better (prohibited).

**Inclusion (in scope for rules):**
- Virulence factor characterization in regulated bacterial or fungal pathogens (FSAP select agents, WHO RG3+)
- Engineering or enhancement of virulence factors for improved pathogen fitness in any host
- Antibiotic or antiviral resistance mechanism studies, and deliberate transfer of resistance to pathogenic organisms
- Immune evasion mechanism characterization and engineering in bacterial and fungal pathogens
- Host-pathogen interaction studies focused on host susceptibility determinants or universal host dependency factors
- Diagnostic biomarker identification and vaccine target research for regulated pathogens (positive end)
- Virulence factor studies in non-select organisms for published academic research (positive end, lower sensitivity)

**Exclusion (out of scope — handled by other domains or unregulated):**
- Viral pathogen virulence and immune evasion → Virology (Domain 1)
- DNA synthesis or genetic engineering of pathogens → Synthetic Biology (Domain 3)
- Sequence-level computational analysis → Genomics (Domain 4)
- Standard clinical microbiology methods (culture, sensitivity testing, susceptibility breakpoints) → unregulated
- Antibiotic mechanism of action for drug development (without resistance-engineering intent) → unregulated
- Host immune response studies without pathogen focus → unregulated immunology

**Primary legitimate use base:** Vaccine target identification, antibiotic drug discovery, clinical diagnostic development, outbreak investigation, and basic microbiology constitute the dominant legitimate use base; this domain is the most over-refusal-prone in bio safety because legitimate virulence biology research vastly outnumbers dual-use research, and rules must maintain a very wide positive prior.

**Boundary with adjacent domains:**
- **Virology:** Pathogen Biology handles bacterial, fungal, and parasitic pathogens; Virology handles viral pathogens exclusively
- **Synthetic Biology:** Pathogen Biology handles natural property characterization; Synthetic Biology handles the engineering of new properties
- **Genomics:** Pathogen Biology handles experimental mechanistic characterization; Genomics handles sequence-level computational prediction

**Key regulatory anchors for this domain:**
- DURC Categories 1, 2, 3, 6 (harmful consequences, immunity disruption, resistance to interventions, host susceptibility)
- FSAP: Bacillus anthracis, Yersinia pestis, Francisella tularensis, Brucella spp., Burkholderia spp., Coxiella burnetii, Coccidioides spp.
- WHO Risk Groups 2–3: M. tuberculosis (RG3), Salmonella (RG2), MRSA (RG2)
- WHO LBM4 risk-based assessment framework: BSL requirements derived from risk assessment, not fixed RG mapping
- FSAP exemptions: vaccine research, diagnostics, published characterization

**Scope note:** Pathogen Biology is the foundational science domain that underpins much of infectious disease medicine: understanding how bacteria cause disease is prerequisite to preventing and treating it. This creates the domain's core challenge — the same knowledge that enables vaccine development and antibiotic discovery could theoretically guide virulence enhancement. The central distinction that structures all rules in this domain is **characterization vs. enhancement**: studying a virulence factor's mechanism in its wild-type context is legitimate science; engineering that factor to increase its potency, host range, or immune evasion is DURC. Rules anchor the positive end on diagnostic biomarker and vaccine target research (explicitly protected under FSAP exemptions) and virulence factor characterization in published literature contexts. They escalate through antibiotic resistance engineering and immune evasion studies, reaching hard-refuse at deliberate virulence factor enhancement. The domain explicitly excludes viral pathogens (Virology), genetic engineering (Synthetic Biology), and sequence-level analysis (Genomics), and maintains an intentionally wide positive prior to avoid systematic over-refusal in this high-volume legitimate-science domain.

---

### Domain 6: Dual-Use Chemistry

**One-sentence definition:** Dual-Use Chemistry covers questions at the chemistry-biology interface — including CWC-scheduled compound synthesis, precursor chemical acquisition, AI-assisted molecular design for toxic bioactivity, and reagent sourcing for biological research — with the central dual-use tension between routine laboratory chemistry (legitimate) and the synthesis or weaponization of chemical agents (prohibited).

**Inclusion (in scope for rules):**
- Synthesis routes and preparation methods for CWC Schedule 1 compounds (nerve agents, mustards, ricin, saxitoxin)
- Structural analog design for Schedule 1 compounds using "general purpose criterion" principles
- Precursor chemical acquisition, sourcing, and combination queries suggesting Schedule 2/3 compound synthesis
- AI-assisted generative chemistry targeting toxicity, lethality, or biological activity optimization
- Delivery system and dispersal mechanism design for chemical agents (aerosolization, particle engineering)
- Reagent sourcing and selection for routine biological research (positive end — default assist with pathogen-context caveat)
- Solvent, buffer, and reagent selection for BSL-2/3 laboratory work

**Exclusion (out of scope — handled by other domains or unregulated):**
- Biological toxin mechanism and delivery → Toxicology (Domain 2)
- Genetic encoding of toxin biosynthesis → Synthetic Biology (Domain 3)
- Standard organic chemistry for pharmaceutical development without Schedule 1 proximity → unregulated
- Agrochemical and pesticide chemistry (organophosphate pesticides below Schedule proximity) → unregulated
- Industrial chemical safety (MSDS, OSHA, process safety) → unregulated
- Food chemistry and natural product isolation → unregulated

**Primary legitimate use base:** Pharmaceutical research, agricultural chemistry, industrial process chemistry, forensic chemistry, and standard laboratory reagent sourcing constitute the dominant legitimate use base; CWC Schedules 2–3 include many common industrial reagents (phosphorus oxychloride, thiodiglycol, phosgene) with entirely legitimate uses, and rules must not block these.

**Boundary with adjacent domains:**
- **Toxicology:** Dual-Use Chemistry handles synthetic organic chemical agents and small-molecule precursors; Toxicology handles protein/peptide biological toxins (botulinum, ricin, SEB)
- **Synthetic Biology:** Dual-Use Chemistry handles small-molecule synthesis; Synthetic Biology handles the biological production of chemicals through engineered organisms
- **Pathogen Biology:** No meaningful boundary overlap; these domains address different threat classes

**Key regulatory anchors for this domain:**
- CWC Article II: definitions of chemical weapons, toxic chemicals, precursors; "general purpose criterion"
- CWC Schedule 1: highest-risk compounds (nerve agents, blister agents, ricin, saxitoxin, BZ); production limit ≤1 MT/year with OPCW declaration
- CWC Schedule 2: moderate-risk precursors (thiodiglycol, PFIB, amiton derivatives); export reporting required
- CWC Schedule 3: dual-use industrial chemicals (phosgene, hydrogen cyanide, chloropicrin); widely produced
- Australia Group: chemical precursor export controls
- CWC Art. II.9(c): explicitly permits protective/detection/medical research on Schedule 1 compounds

**Scope note:** Dual-use chemistry in the biosecurity context sits at the intersection of organic chemistry, biochemistry, and international arms control law. The CWC provides the primary legal framework, with three schedules reflecting decreasing restriction based on legitimate civilian use: Schedule 1 compounds have few or no civilian applications and face near-absolute synthesis restrictions; Schedule 2 compounds are significant precursors requiring export reporting; Schedule 3 compounds are widely produced industrially and require lighter controls. The domain's key challenge is the "general purpose criterion" (CWC Art. II.1) — any chemical can theoretically be a weapon if used as such, but this cannot justify blanket restriction of chemistry. Rules must operationalize the criterion by combining (Schedule proximity) × (quantity and context) × (delivery/dispersal framing). The hardest cases are Schedule 1 synthesis requests, where the combination of compound identity and synthesis guidance leaves no legitimate framing. Mid-range cases involve precursor sourcing and AI-assisted molecular design, where optimization target and context determine severity. The positive anchor is routine reagent sourcing for biological research, where the question is standard lab practice and the pathogen context (if any) provides the caveat, not the chemistry itself. The domain explicitly excludes biological protein toxins (Toxicology) and standard agrochemical/pharmaceutical chemistry that falls well below Schedule proximity.
