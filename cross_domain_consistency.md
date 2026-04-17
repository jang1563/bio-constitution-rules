# Cross-Domain Consistency — Severity Tier Rationale

This document records the cross-domain consistency check for the 30 rules in the Bio Constitution Rules Library. Its purpose is to ensure that equivalent-risk scenarios across different bio domains receive equivalent severity tiers, and to document any intentional tier differences.

---

## 1. Equivalent-Risk Pairings — Verified

The following pairs address equivalent-risk scenarios in different domains. Both rules in each pair were verified to carry the same severity tier.

| Risk scenario | Domain A rule | Domain B rule | Tier | Rationale for parity |
|---------------|--------------|--------------|------|----------------------|
| Delivery mechanism design for a dangerous agent | T04 (toxin dispersal, hard-refuse) | C04 (chemical agent delivery, hard-refuse) | hard-refuse | Both rules: stated agent + delivery framing = weaponization. CWC Art. II.1(b)/(c) covers both biological toxins and chemical agents in the same framework |
| Enhancement of dangerous biological properties | V01 (airborne transmission, hard-refuse) | P02 (virulence enhancement, hard-refuse) | hard-refuse | DURC Cat 4/1 respectively; both represent the highest-concern DURC research; no legitimate framing resolves either |
| Lethality/potency optimization | T02 (toxin SAR for lethality, hard-refuse) | C01 (CWC Schedule 1 synthesis, hard-refuse) | hard-refuse | Both optimize toward maximum harm potential; no non-weapons legitimate use; treaty-covered |
| Reconstruction of eradicated/extinct dangerous agent | V04 (viral reconstitution, hard-refuse) | S01 (de novo synthesis of select agent genome, hard-refuse) | hard-refuse | Both are DURC Cat 7 analogs; functional equivalence of natural reconstitution and synthetic route |
| AI-assisted design of novel dangerous agents | G02 (AI sequence design, hard-refuse) | C03 (AI molecular design for toxicity) | G02: hard-refuse; C03: decline-with-alternative | Intentional difference — see Section 2 |
| Resistance engineering in dangerous organisms | P03 (AMR engineering, decline) | S04 (CRISPR editing regulated pathogens, decline) | decline-with-alternative | Both have large legitimate alternative spaces; FSAP registration is the legitimate pathway for both |
| Host range / cross-species alteration | V02 (host range alteration, decline) | G03 (pandemic potential prediction, decline) | decline-with-alternative | Both: retrospective analysis assisted; prospective optimization declined; escalation to hard-refuse on explicit optimization framing |
| Immune evasion engineering | V03 (viral immune evasion, decline) | P04 (bacterial/fungal immune evasion, decline) | decline-with-alternative | DURC Cat 2 in both; characterization permitted; engineering declined |
| Synthesis screening circumvention | S01 (genome synthesis, hard-refuse) | S03 (directed evolution as synthesis workaround, decline→hard-refuse escalation) | S01: hard-refuse; S03: decline-with-alternative with hard-refuse escalation | Intentional nuance — see Section 2 |
| Legitimate mechanism-of-action understanding | T01 (toxin mechanism, assist-with-caveats) | C01 EC2 (nerve agent mechanism for antidote, assist-with-caveats) | assist-with-caveats | Both: CWC Art. II.9(b) explicitly permits; mechanism ≠ synthesis; key dual-use distinction |
| Vaccine/diagnostic target identification | V05 (vaccine antigen design, assist-with-caveats) | P05 (diagnostic biomarker/vaccine target, assist-with-caveats) | assist-with-caveats | Both anchor the positive end; large legitimate base; pathogen identity + enhancement framing are the only resolvers |

---

## 2. Intentional Tier Differences

The following apparent inconsistencies are intentional — each is documented with rationale.

### G02 (hard-refuse) vs. C03 (decline-with-alternative)

**G02** — AI-assisted de novo design of novel dangerous pathogen sequences: **hard-refuse**  
**C03** — AI-assisted molecular design targeting toxic bioactivity: **decline-with-alternative**

**Rationale:** The severity difference reflects the upstream capability gap. Designing a novel pathogen sequence from scratch (G02) is directly equivalent to S01 (full-genome synthesis from scratch) and requires no intermediate laboratory step — the designed sequence is the threat vector. In contrast, C03 (AI molecular design for toxicity) requires downstream synthesis and testing to realize harm; the designed molecule is not itself a weapon. The alternative in C03 is genuine: pharmacological optimization tools can be redirected to non-toxic targets. There is no equivalent alternative for G02 — designing a "less dangerous novel pathogen sequence" does not serve the same research function.

**Escalation:** Within C03, hard-refuse applies when the optimization target is explicit AChE inhibition (Schedule 1 analog) — bridging C03 to C01 territory.

---

### S03 (decline-with-alternative + hard-refuse escalation) vs. S01 (hard-refuse)

**S01** — De novo synthesis of select agent genome sequences: **hard-refuse**  
**S03** — Directed evolution of virulence factors or toxin potency: **decline-with-alternative** (with hard-refuse escalation for FSAP Tier 1 virulence factor or CWC Schedule 1 toxin potency)

**Rationale:** Directed evolution has a large legitimate application space — protein engineering, industrial enzyme improvement, directed evolution in non-pathogen systems. The base tier for S03 is decline-with-alternative because the alternative (directed evolution in non-pathogen organisms) is scientifically substantive. The hard-refuse escalation applies specifically when the evolution target is an FSAP Tier 1 virulence factor or CWC Schedule 1 toxin potency — at that point the activity is functionally equivalent to T02 (lethality optimization) or P02 (virulence enhancement), both hard-refuse. The parent rule is decline-with-alternative because the topic class (directed evolution) is broad; the specific escalation cases that trigger hard-refuse are narrow and explicit.

---

### V03 (decline-with-alternative) vs. V01 (hard-refuse)

**V01** — Airborne transmission enhancement: **hard-refuse**  
**V03** — Immune evasion mechanism characterization vs. engineering: **decline-with-alternative**

**Rationale:** Transmissibility enhancement (V01) is DURC Cat 4 — directly increasing a pathogen's ability to spread. Immune evasion characterization (V03) spans a wide range from fully legitimate (understanding natural immune evasion in published isolates) to concerning (engineering immune escape in FSAP Tier 1 pathogens). The large legitimate base in vaccine design and natural variant surveillance justifies decline-with-alternative as the base tier. Hard-refuse escalation within V03 applies when the query involves FSAP Tier 1 viral pathogens with explicit engineering design for immune escape — at that point it converges with V01 (DURC Cat 4/2 combined). Airborne transmission has no legitimate framing that resolves the concern; immune evasion characterization does.

---

### G04 (assist-with-caveats) vs. G01 (decline-with-alternative)

**G01** — Functional annotation of select agent genomes: **decline-with-alternative**  
**G04** — Variant effect prediction for pathogen virulence determinants: **assist-with-caveats**

**Rationale:** G04 covers VEP for known proteins in characterized virulence factors — the legitimate scientific base (HIV drug resistance monitoring, SARS-CoV-2 vaccine update guidance) is enormous. G01 covers annotation of unknown sequences in select agent genomes, where the output could itself define new enhancement targets. The distinction is: VEP predicts effects of variants in proteins with known function (G04, high legitimate base); functional annotation assigns function to unannotated elements (G01, higher dual-use concern because it may identify novel virulence determinants). The boundary is explicitly cross-referenced in G04's resolving context table: VEP applied to novel unannotated ORFs in select agent genomes escalates to G01.

---

## 3. Severity Tier Distribution

```
hard-refuse (9):
  V01, V04              — virology hard floor (airborne enhancement, extinct reconstitution)
  T02, T04              — toxicology hard floor (lethality optimization, dispersal)
  S01                   — synthetic biology hard floor (full-genome synthesis)
  G02                   — genomics hard floor (AI novel pathogen design)
  P02                   — pathogen biology hard floor (virulence enhancement)
  C01, C04              — chemistry hard floor (CWC Sched 1 synthesis, delivery)

decline-with-alternative (12):
  V02, V03              — virology: host range, immune evasion (large legitimate base + alternative)
  T03                   — toxicology: production scale-up (FSAP registration pathway is real alternative)
  S02, S03, S04         — synthetic biology: circuit design, directed evolution, CRISPR
  G01, G03              — genomics: annotation, pandemic potential (retrospective assists)
  P03, P04              — pathogen biology: AMR engineering, immune evasion (surveillance alternatives)
  C02, C03              — chemistry: precursor sourcing, AI molecular design

assist-with-caveats (7):
  V05                   — virology positive anchor (vaccine antigen design)
  T01, T05              — toxicology positive anchors (mechanism, antidote)
  G04                   — genomics positive anchor (VEP for clinical/surveillance)
  P01, P05              — pathogen biology positive anchors (virulence characterization, diagnostics)
  C05                   — chemistry positive anchor (routine reagents)

warn-and-assist (2):
  S05                   — synthetic biology positive anchor (metabolic engineering, non-pathogen synbio)
  G05                   — genomics positive anchor (metagenomics, environmental surveillance)
```

**Positive-end anchors by domain:** Every domain has at least one assist or warn tier rule. This prevents the library from generating only refusal training data.

---

## 4. DURC Category Coverage

| DURC Category | Definition | Rules |
|--------------|-----------|-------|
| Cat 1 — enhance harmful consequences | Increase severity, lethality, or morbidity | P02 (primary), T02 (toxin), V01 (partial), S03 (escalation) |
| Cat 2 — disrupt immune response | Impair innate/adaptive immunity to protect the pathogen | V03, P04 |
| Cat 3 — resistance to interventions | Confer resistance to antibiotics, antivirals, or vaccines | P03 |
| Cat 4 — transmissibility/stability/dissemination | Enhance spread, stability in environment, or aerosolization | V01 (primary), S02 (edge case) |
| Cat 5 — host range/tropism | Alter ability to infect new host species | V02 (primary), G03 (computational prediction) |
| Cat 6 — enhance host susceptibility | Make host population more susceptible | No dedicated rule — edge cases in P03, P04 (see `phase1/topic_rationale.md`) |
| Cat 7 — reconstitute eradicated agent | Rebuild a pathogen that no longer exists in nature | V04, S01, G02 |

---

## 5. Adversarial Review Summary

Four adversarial review passes were conducted after initial rule drafting:

1. **Red-team loophole finder** — tested rules for framing exploits (academic, historical, computational, defensive-purpose framings)
2. **Over-refusal auditor** — identified rules that blocked legitimate science without justification
3. **Regulatory accuracy auditor** — verified all CWC article numbers, FSAP thresholds, attribution of historical synthesis events
4. **Cross-domain consistency auditor** — verified severity tier parity across equivalent-risk scenarios

Key corrections from review:
- CWC Art. II.9(c) → II.9(b) (protective purposes provision): corrected across 5 rules
- CWC Art. II.2 → II.1 (general purpose criterion location): corrected in C01
- CWC Art. II.1(a)(ii)/(iii) → II.1(b)/(c) (delivery equipment): corrected in T04
- FSAP possession thresholds: ricin/abrin/saxitoxin/tetrodotoxin corrected to 100 mg (not 5 mg); T-2 toxin added at 1,000 mg
- IGSC (not IASB): synthesizing body corrected in S01, S03, G02
- University of Alberta horsepox synthesis (Noyce et al., 2018) — not CSIRO: attribution corrected in V04, S01
- S03 directed evolution severity: escalation to hard-refuse added for FSAP Tier 1 virulence factors and CWC Schedule 1 toxin potency
- S04 CRISPR rule: non-FSAP pathogenic organisms with loss-of-function edits reclassified to assist-with-caveats (was decline-with-alternative — over-refusal)
- S01 EC1: single gene codon optimization for non-toxic proteins from FSAP pathogens reclassified to assist-with-caveats (was blanket decline — over-refusal)
- G03: natural wild-type HPAI H5N1 isolate comparison using published WHO/CDC frameworks (IRAT, TIPRA) reclassified to assist-with-caveats (was decline — over-refusal)
- T03 EC1: sub-FSAP-threshold preparation for validated analytical use in institutional laboratory reclassified to assist-with-caveats (was decline — over-refusal)
- V01 JSON: `HPAI_H5N7` → `HPAI_H5_H7` (correct strain designation)
