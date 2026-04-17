# Phase 1: Topic Selection Rationale and Coverage Analysis

> **Generated:** 2026-04-16
> **Purpose:** Audit trail for the 30-topic selection. Explains selection criteria application, coverage checks, and cross-domain consistency decisions. Supports expert reviewer framing and application differentiation.

---

## 1. Selection Criteria Applied

Each of the 30 topics was evaluated against five criteria:

| Criterion | What it means | How applied |
|-----------|--------------|-------------|
| **Frequency** | Claude faces this decision type regularly | Retained: transmission enhancement, CRISPR editing, reagent sourcing. Excluded: hypothetical novel weapon types with no prior query examples |
| **Ambiguity** | The right answer is non-obvious without biological reasoning | Retained: V03 (immune evasion: characterization vs. engineering), P01 (virulence characterization vs. enhancement). Excluded: clear-cut cases covered by default behavior |
| **Regulatory grounding** | ≥1 NSABB/FSAP/BWC/CWC/AG anchor exists | All 30 topics satisfy this; regulatory anchors listed in `rule_topics_master.md` |
| **Severity coverage** | Topics collectively span all 4 tiers within each domain | Met: each domain has ≥1 positive rule and ≥1 hard or decline rule |
| **Legitimate-use balance** | Each domain has ≥1 topic anchoring the positive end | Met: V05, T01, T05, G04, G05, P01, P05, C05, S05 are positive-end anchors |

---

## 2. Topic Selection Decisions — By Domain

### Virology (V01–V05)

**Why these 5:**
- **V01 (airborne transmission):** The Fouchier/Kawaoka H5N1 controversy is the defining case that established modern DURC policy; Claude faces this class of query regularly from both legitimate researchers and potential misuse actors. Hard-refuse with no resolving context.
- **V02 (host range):** The second most common virology GOF query type; the ambiguity between wild-type characterization (observing natural host range) and engineering (creating new host range) is the central challenge. Decline-with-alternative.
- **V03 (immune evasion):** Large legitimate base (vaccine research identifies immune evasion as drug targets) with dangerous edge (engineering immune escape). Rich resolving context via vaccine/antiviral development framing. Decline-with-alternative.
- **V04 (reconstitution):** Tests the absolute prohibition. Variola and 1918 flu are the canonical cases; no context resolves this. Hard-refuse.
- **V05 (vaccine antigen design):** Anchors the positive end. Without this rule, the virology domain would be entirely restrictive, creating systematic over-refusal. The rule must exist to explicitly facilitate legitimate vaccine research, which is the dominant use case for virology questions.

**Topics considered and excluded:**
- Serial passage for adaptation: Covered as edge case of V01 (airborne transmission) and V02 (host range); a dedicated rule would be redundant.
- Chimeric virus construction: Covered as edge case of V02 + V03; a dedicated rule would add one more Decline-with-alternative without adding tier diversity.
- Standard plaque assay/TCID50 methods: No rule needed — default assist applies; no DURC concern.

---

### Toxicology (T01–T05)

**Why these 5:**
- **T01 (mechanism of action):** Antidote development, cancer therapy (immunotoxins/ADCs), and neuroscience require toxin mechanism understanding. The rule must explicitly assist this large legitimate base. Assist-with-caveats.
- **T02 (SAR for lethality):** The hard floor. Potency optimization for listed toxins has no legitimate framing. Hard-refuse.
- **T03 (production thresholds):** The FSAP threshold logic is the primary regulatory decision variable for toxins; a rule encoding the mg-level thresholds is essential for accurate severity tiering. Decline-with-alternative.
- **T04 (delivery/dispersal):** Listed toxin + dispersal mechanism = weaponization signal. Parallels V01 and C04 in logical structure. Hard-refuse.
- **T05 (antidote/countermeasure):** Explicitly permitted under CWC Art. II.9(c); one of the largest legitimate biosafety research use cases. Anchors the positive end alongside T01.

**Topics considered and excluded:**
- Novel toxin synthesis (non-listed): Covered as edge case of T02 (SAR for lethality) via structural analog principle.
- Environmental toxin monitoring: No rule needed — default assist; no regulatory concern.

---

### Synthetic Biology (S01–S05)

**Why these 5:**
- **S01 (de novo synthesis):** The hard floor for synthetic biology; IASB screening exists precisely for this case. Hard-refuse.
- **S02 (genetic circuit design):** Common academic query (iGEM-adjacent); the chassis organism identity + modification type create meaningful ambiguity. Decline-with-alternative.
- **S03 (directed evolution):** Directed evolution is functionally equivalent to synthesis screening bypass when applied to virulence factors; Claude must recognize this workaround pattern. Decline-with-alternative.
- **S04 (CRISPR):** CRISPR ubiquity makes this the most-queried synthetic biology topic; institutional containment approval is the key resolving context. Decline-with-alternative.
- **S05 (metabolic engineering):** Anchors the positive end; the enormous legitimate base of industrial and pharmaceutical synthetic biology must be explicitly facilitated. Warn-and-assist.

**Topics considered and excluded:**
- Gene drive development: Covered as edge case of S02 (genetic circuit design with ecological release framing); a dedicated rule would be too narrow for the 30-rule scope.
- Cell-free biosynthesis of toxins: Covered as edge case of T03 (production thresholds) and S02 (genetic circuit producing toxins).

---

### Genomics (G01–G05)

**Why these 5:**
- **G01 (functional annotation):** NCBI/GISAID data access makes this a common query type; published annotation (legitimate) vs. novel enhancement-predicting annotation (DURC per NSABB 2023) is the central ambiguity. Decline-with-alternative.
- **G02 (AI-assisted de novo design):** The fastest-growing dual-use risk; Claude is directly in this loop. No resolving context justifies de novo design of sequences encoding pandemic pathogens. Hard-refuse.
- **G03 (pandemic potential prediction):** The NSABB 2023 frontier: sequence → pandemic potential is the new form of DURC concern. Frequent in computational biology. Decline-with-alternative.
- **G04 (VEP for virulence):** Standard bioinformatics with a large legitimate base; elevated sensitivity in virulence context; resolving context is pathogen identity + downstream application. Assist-with-caveats.
- **G05 (metagenomics):** Environmental surveillance is predominantly legitimate; the positive prior is strong; downstream isolation escalates. Warn-and-assist.

**Topics considered and excluded:**
- Population genomics for ethnic targeting: Too speculative as a current risk; covered as edge case of G02 (AI-assisted design) if applicable.
- Phylogenetic analysis for outbreak attribution: No rule needed — default assist; public health use is primary.

---

### Pathogen Biology (P01–P05)

**Why these 5:**
- **P01 (virulence characterization):** The most over-refusal-prone topic in biosafety; a rule explicitly facilitating legitimate characterization research is essential to avoid systematic under-service of the field. Assist-with-caveats.
- **P02 (virulence enhancement):** The hard floor; the line between P01 and P02 is the domain's central question. Hard-refuse.
- **P03 (resistance engineering):** DURC Cat 3; discovery of natural resistance (legitimate) vs. deliberate engineering and transfer (DURC) is the ambiguity common in clinical microbiology. Decline-with-alternative.
- **P04 (immune evasion):** Bacterial/fungal analog of V03; understanding immune evasion for vaccine targets is legitimate, engineering it is DURC Cat 2. Decline-with-alternative.
- **P05 (diagnostic/vaccine target):** Explicitly protected; anchors the positive end; global health priority. Assist-with-caveats.

**Topics considered and excluded:**
- Host factor identification for pathogen entry: Covered as edge case of P01 (virulence characterization) — host factors that enable infection are a type of virulence determinant.
- Sporulation/latency biology: Too narrow; covered as part of P01's broad scope.

---

### Dual-Use Chemistry (C01–C05)

**Why these 5:**
- **C01 (Schedule 1 synthesis):** The absolute floor; treaty-prohibited synthesis. Hard-refuse.
- **C02 (Schedule 2/3 precursors):** The volume of chemistry dual-use concern lives here; sourcing pattern + quantity + context drive severity. Decline-with-alternative.
- **C03 (AI-assisted toxic design):** The Urbina et al. case study empirically demonstrated this risk; Claude is in this loop. Decline-with-alternative.
- **C04 (delivery/dispersal):** Parallels T04 in logical structure; delivery + chemical agent = weaponization. Hard-refuse.
- **C05 (routine reagent sourcing):** Anchors the positive end; the overwhelming majority of reagent questions are legitimate. Assist-with-caveats.

**Topics considered and excluded:**
- Novel chemical weapon synthesis (non-scheduled): Covered by C01 via "general purpose criterion" and structural analog principle.
- Standard pharmaceutical chemistry: No rule needed — default assist; no Schedule proximity.

---

## 3. Severity Tier Distribution

| Tier | Count | Distribution (%) | Notes |
|------|-------|-----------------|-------|
| Hard-refuse | 9 | 30% | Higher than typical content classification because bio domain safety is asymmetrically weighted toward harm prevention |
| Decline-with-alternative | 12 | 40% | The largest tier; these rules generate the most useful synthetic training data because they have rich resolving context |
| Assist-with-caveats | 7 | 23% | Anchors the positive end; essential to prevent systematic over-refusal |
| Warn-and-assist | 2 | 7% | The two lowest-sensitivity positive rules (S05, G05); limited to domains where the legitimate science base is so enormous that even minimal restriction signal is warranted |

**Why 9 hard-refuse rules (vs. typical binary classifiers):**
Most content safety classifiers use a binary allow/block scheme. The 4-tier system here reflects the biological reality that the space between "clearly fine" and "clearly prohibited" is large and populated by queries that deserve different responses than either extreme. The 9 hard-refuse rules represent the subset of biological dual-use concern where expert consensus (DURC Cat 7, CWC Schedule 1, ePPP reconstitution) is that no contextual information can justify the assistance.

---

## 4. DURC Category Coverage

| DURC Category | Definition | Rules addressing it | Coverage type |
|--------------|-----------|--------------------|----|
| Cat 1: Enhance harmful consequences | P02 (virulence enhancement), T02 (toxin potency optimization), V01 (partial: transmissibility increases harm) | Direct (P02, T02); partial (V01) | Strong |
| Cat 2: Disrupt immunity | V03 (viral immune evasion), P04 (bacterial/fungal immune evasion) | Direct | Strong |
| Cat 3: Resistance to interventions | P03 (antibiotic/antiviral resistance engineering) | Direct | Strong |
| Cat 4: Transmissibility/stability/dissemination | V01 (airborne transmission — the canonical Cat 4 case), S02 (edge case: circuit design for transmissibility) | Direct (V01); edge case (S02) | Adequate |
| Cat 5: Host range/tropism | V02 (host range alteration — direct), G03 (sequence-based prediction of host range) | Direct (V02); computational analog (G03) | Adequate |
| Cat 6: Enhance host susceptibility | No dedicated rule — addressed in edge case annotations of P03 and P04 | Edge case only | Intentional gap (see rationale below) |
| Cat 7: Reconstitute eradicated agent | V04 (viral reconstitution), S01 (synthetic reconstruction), G02 (AI-assisted sequence design) | Direct (3 rules) | Strong |

**Rationale for Cat 6 gap:** DURC Category 6 ("enhance the susceptibility of a host population to the agent or toxin") is the least commonly encountered DURC category as a research question type. It would manifest as research that immunosuppresses populations or impairs innate immunity to make them more susceptible to a listed pathogen — an unusual experimental framing that does not appear frequently in Claude interactions. A dedicated rule would generate little useful synthetic training data and would likely have implausibly narrow edge cases. Cat 6 is adequately addressed as an edge case in P03 (resistance engineering that renders hosts unable to respond) and P04 (immune evasion enhancement that functionally increases host susceptibility). This is intentional scope narrowing documented transparently.

---

## 5. Cross-Domain Consistency — Severity Tier Alignment

Equivalent-risk scenarios across domains must receive equivalent tiers. These pairings were checked for consistency:

| Scenario pair | Rules | Severity | Consistent? | Rationale |
|---------------|-------|---------|------------|-----------|
| Delivery mechanism (biological) | T04 (toxin dispersal) | Hard-refuse | — | — |
| Delivery mechanism (chemical) | C04 (chemical agent delivery) | Hard-refuse | ✓ | Same logical structure: agent identity + delivery framing = weaponization |
| Enhancement of dangerous properties (virus) | V01 (airborne transmission) | Hard-refuse | — | — |
| Enhancement of dangerous properties (bacteria) | P02 (virulence enhancement) | Hard-refuse | ✓ | Same DURC Cat 1/4 structure regardless of pathogen type |
| Positive characterization (virology) | V05 (vaccine antigen design) | Assist-with-caveats | — | — |
| Positive characterization (pathogen biology) | P01 (virulence characterization) | Assist-with-caveats | ✓ | Both are characterization-not-enhancement with large legitimate base |
| Synthesis of prohibited compound (bio) | S01 (select agent synthesis) | Hard-refuse | — | — |
| Synthesis of prohibited compound (chem) | C01 (Schedule 1 synthesis) | Hard-refuse | ✓ | Both are treaty-prohibited synthesis |
| AI-assisted dangerous design (bio sequence) | G02 (novel pathogen sequence design) | Hard-refuse | — | — |
| AI-assisted dangerous design (chemistry) | C03 (toxic molecular design) | Decline-with-alternative | ✗ (intentional) | Chemistry has richer resolving context (optimization target, structural proximity) than biology; bio = closest structural analog to CWC Sched 1 = Hard-refuse |
| Precursor/circuit with partial concern | S02 (genetic circuit), C02 (precursor sourcing) | Decline-with-alternative | ✓ | Parallel structure: partial information with resolving context available |
| Large legitimate base with caveat | P05 (diagnostic/vaccine targets), T05 (antidote research) | Assist-with-caveats | ✓ | Both explicitly protected by FSAP exemptions and international law |

**Intentional asymmetry (G02 vs. C03):** G02 (AI-assisted novel pathogen design) is Hard-refuse while C03 (AI-assisted toxic molecular design) is Decline-with-alternative. This is intentional: biological sequence design for novel dangerous pathogens has no resolving context (you cannot provide "legitimate" guidance for creating a novel pandemic pathogen); AI-assisted toxic molecular design does have resolving context (optimization target, structural distance from Schedule 1, stated therapeutic purpose), making decline-with-alternative the appropriate tier.

---

## 6. Comparative Calibration — vs. Existing Classifiers

| Classifier | Bio categorization | Severity granularity | Biological reasoning | Regulatory mapping | This rule set |
|------------|------------------|---------------------|---------------------|-------------------|---------------|
| Llama Guard 3 | Single "WMD Uplift" bucket | Binary | None | None | 6-domain decomposition, 4 tiers, reasoning per rule, per-rule regulatory citation |
| WildGuard | "CBRN" bucket | Binary | None | None | Same improvements |
| WMDP | 3 domains (bio/chem/cyber) | N/A (eval only) | None | None | 6 bio sub-domains, severity calibrated to DURC categories |
| Constitutional BioGuard | 7 NSABB DURC categories | Binary | Not published | Not published | Adds: 4-tier system, biological reasoning per rule, edge case annotations, explicit regulatory citations |

This rule set adds value over all existing systems primarily through: (1) domain decomposition, (2) biological reasoning, (3) severity tiers, (4) explicit regulatory mapping, and (5) edge case documentation.

---

## 7. Ready for Phase 3

**Phase 1 is complete** when this file and `domain_scopes.md` and `rule_topics_master.md` are finalized.

**Phase 2 (regulatory baseline extraction):** Can proceed in parallel with Phase 3 early rules. Read `research/regulatory/*.md` and cross-reference each topic row in `rule_topics_master.md` to produce `regulatory_mapping.md`.

**Phase 3 (rule drafting):** Begin with V01–V05 (stress-test the 10-field rule template). Order: V01 → V02 → V03 → V04 → V05 → then T01–T05 → S01–S05 → G01–G05 → P01–P05 → C01–C05. Each rule is ~250–400 words in markdown. Target ~750 words total per rule including JSON representation.
