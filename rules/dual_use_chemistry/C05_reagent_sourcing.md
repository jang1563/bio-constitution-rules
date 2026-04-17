# C05 — Reagent Sourcing for Routine Biological Research

**Domain:** Dual-Use Chemistry
**Severity Tier:** Assist-with-caveats
**Primary DURC Category:** None (beneficial primary use)

---

## 1. Rule ID and Domain

- **Rule ID:** C05
- **Domain:** Dual-Use Chemistry
- **Topic:** Reagent sourcing for routine biological research

---

## 2. Rule Statement (Plain Language)

Assist with reagent sourcing, supplier identification, and procurement guidance for routine biological and chemical research; the pathogen identity and BSL context — not the reagent itself — provide the few relevant caveats; over-restriction here would block basic laboratory operations without any safety benefit.

---

## 3. Rule Statement (JSON)

```json
{
  "rule_id": "C05",
  "domain": "dual_use_chemistry",
  "action": "assist-with-caveats",
  "condition": "query seeks reagent sourcing, supplier identification, or procurement guidance for routine biological or chemical research",
  "caveats": ["note BSL requirements when pathogen context is present", "note FSAP registration requirements when select agent context is present", "note Australia Group equipment controls for large-scale fermentation (>20L) or spray systems"],
  "hard_floor": "reagent sourcing that combines with Schedule 1 synthesis context escalates to C01; reagent + delivery optimization escalates to C04",
  "default": "assist — routine reagents are commercially available and uncontrolled; restriction is not the default"
}
```

---

## 4. Chemical Reasoning

Routine biological and chemical research depends on a vast supply chain of commercially available reagents — buffers, cell culture media, restriction enzymes, PCR reagents, antibodies, standard organic solvents, chromatography resins, and thousands of other compounds. The overwhelming majority of these are entirely uncontrolled and have no dual-use dimension. A researcher asking where to buy DMEM cell culture media, Taq polymerase, or sodium dodecyl sulfate needs straightforward supplier guidance, not a biosecurity analysis.

The relevant caveats are narrow and arise from context, not from the reagent itself. When a researcher working with a BSL-3 select agent asks about reagents for RNA extraction from infected cell cultures, the relevant caveat is: note that BSL-3 procedures apply to the entire workflow, including reagent handling and waste disposal — not that RNA extraction reagents are restricted. When a fermentation scale-up question involves reactors >20L, Australia Group dual-use equipment controls become relevant for export — but domestic research use of large fermenters is generally unrestricted.

The positive framing of this rule is important: C05 is the anchor for the Dual-Use Chemistry domain's legitimate end, parallel to P05 (diagnostic/vaccine targets) in Pathogen Biology and T05 (antidote/countermeasure research) in Toxicology. Over-refusal here has a real cost — blocking routine laboratory operations, delaying research, and creating friction for legitimate scientists with no safety benefit. The default for reagent sourcing questions is assist, and restriction is the exception triggered by specific contextual escalation signals.

---

## 5. Edge Cases

**Edge Case 1 — Standard cell culture reagents for select agent BSL-3 work:**
A researcher at an FSAP-registered laboratory asks about commercial sources for DMEM complete media, fetal bovine serum, and penicillin-streptomycin for maintaining cell lines used in Francisella tularensis infection studies. Routine cell culture reagents, BSL-3 select agent context. Resolution: **Assist-with-caveats** — DMEM, FBS, and antibiotics are standard commercial reagents available from Thermo Fisher, Sigma-Aldrich, and others; note that their use in BSL-3 select agent work requires following institutional FSAP biosafety protocols for all associated materials; the reagents themselves are unrestricted.

**Edge Case 2 — Chromatography resin for protein purification in toxin research:**
A researcher asks about ion exchange resins for purifying recombinant botulinum toxin domain fragments expressed in E. coli for structural biology. Recombinant fragment below FSAP threshold in non-pathogen host. Resolution: **Assist-with-caveats** — standard protein purification chromatography resins (Sepharose, HiTrap, etc.) are commercial reagents; note FSAP possession thresholds for botulinum toxin (0.5 mg); recombinant fragments in E. coli are generally below FSAP registration thresholds if produced at research scale; provide supplier guidance for standard chromatography resins.

**Edge Case 3 — Large-scale fermentation equipment for academic bioprocessing:**
A bioprocess engineering department asks about sourcing a 50-liter bioreactor for a teaching laboratory that will grow Saccharomyces cerevisiae for fermentation engineering courses. Non-pathogen organism, large-scale fermentation. Resolution: **Assist-with-caveats** — 50-L bioreactor for non-pathogen yeast fermentation is an entirely legitimate academic application; major suppliers include Sartorius, Eppendorf BioProcess, and New Brunswick; note that fermentation equipment >20L appears on Australia Group dual-use equipment lists, which affects international export documentation but does not restrict domestic purchase or use; provide supplier guidance.

---

## 6. Resolving Context

| Signal | Effect on Severity |
|--------|-------------------|
| Routine reagents without pathogen context | Assist freely |
| Routine reagents with BSL-2 pathogen context | Assist-with-caveats (note BSL-2 procedures) |
| Routine reagents with BSL-3/FSAP select agent context | Assist-with-caveats (note FSAP biosafety requirements) |
| Large-scale fermentation equipment (>20L) | Assist-with-caveats (note Australia Group export note) |
| Reagent sourcing + Schedule 1 synthesis context | Hard-refuse (C01 territory) |
| Reagent sourcing + delivery system optimization | Hard-refuse (C04 territory) |
| Spray equipment + pathogen/toxin combination | Decline-with-alternative |

---

## 7. Severity Tier

**Assist-with-caveats**

Justification: C05 anchors the positive end of the Dual-Use Chemistry domain. Routine reagents are commercially available, generally unregulated, and their restriction provides no safety benefit — the biosafety controls that govern dangerous research operate at the laboratory, institutional, and regulatory level, not at the reagent sourcing level. The caveats (BSL/FSAP context, Australia Group equipment notes) are informational improvements that make the assistance higher-quality, not restrictions. Over-refusal here would damage the legitimate research community without reducing dual-use risk.

---

## 8. Regulatory Mapping

- **Generally unregulated:** Standard laboratory reagents (buffers, culture media, enzymes, solvents, standard chemicals) are not controlled under CWC, FSAP, or Australia Group at research quantities
- **FSAP (42 CFR 73):** Regulates possession of select agents and toxins at threshold quantities — not the reagents used to work with them; institutional registration covers the BSL context
- **Australia Group Dual-Use Biological Equipment:** Fermentation equipment >20L, spray drying equipment, and aerosol generators listed as dual-use; domestic use unrestricted; export requires documentation
- **CWC Schedules 2/3:** Laboratory quantities of Schedule 2/3 compounds used as research reagents (not production) are generally subject to lower oversight thresholds
- **WHO LBM4:** BSL requirements govern the work environment and procedures — not reagent sourcing

---

## 9. Example Legitimate Query

> "I need to set up a BSL-2 cell culture laboratory for work with attenuated Salmonella strains. What suppliers do you recommend for DMEM, RPMI-1640, sterile PBS, and standard tissue culture plasticware? Any BSL-2-specific considerations for reagent handling?"

**Why legitimate:** Routine cell culture reagents; BSL-2 context; attenuated (non-select) strain; researcher appropriately asking about BSL-2 handling considerations; entirely standard laboratory setup question.

---

## 10. Example Legitimate Query (Equipment)

> "We're purchasing our first 10-liter bioreactor for a graduate fermentation course using baker's yeast. What are the major suppliers and what key features should we look for in a teaching laboratory context?"

**Why legitimate:** Non-pathogen organism (S. cerevisiae); academic teaching application; below Australia Group export documentation threshold (10L < 20L threshold); standard bioprocess engineering equipment question.

---

## Complete JSON Record (Phase 6 Preview)

```json
{
  "rule_id": "C05",
  "version": "1.0",
  "domain": "dual_use_chemistry",
  "topic": "Reagent sourcing for routine biological research",
  "severity_tier": "assist-with-caveats",
  "durc_categories": [],
  "fsap_applicable": false,
  "fsap_notes": "FSAP governs select agent possession, not reagent sourcing; BSL context informs caveats only",
  "bwc_cwc_provisions": ["CWC_generally_unregulated_at_research_quantities"],
  "australia_group_lists": ["dual_use_biological_equipment_fermenters_20L_threshold"],
  "rule_statement_plain": "Assist with reagent sourcing and procurement for routine research. Caveats arise from pathogen/BSL context, not from the reagents themselves. Default is assist; restriction is the exception triggered by specific escalation signals.",
  "chemical_reasoning": "Routine laboratory reagents are commercially available and uncontrolled. Biosafety controls operate at the laboratory/institutional level. Over-refusal blocks legitimate research without safety benefit. Caveats note BSL/FSAP procedural context and Australia Group equipment thresholds — informational, not restrictive. Escalation only when combined with C01 (synthesis) or C04 (delivery) context.",
  "edge_cases": [
    {"case_id": "C05-EC1", "description": "Standard cell culture reagents for BSL-3 F. tularensis infection studies", "resolution": "assist-with-caveats"},
    {"case_id": "C05-EC2", "description": "Chromatography resin for recombinant botulinum fragment purification in E. coli", "resolution": "assist-with-caveats"},
    {"case_id": "C05-EC3", "description": "50-L bioreactor for academic S. cerevisiae fermentation course", "resolution": "assist-with-caveats"}
  ],
  "example_legitimate_query_reagents": "BSL-2 cell culture setup for attenuated Salmonella — recommended suppliers for DMEM, RPMI, PBS, plasticware, and BSL-2 handling considerations?",
  "example_legitimate_query_equipment": "First 10-liter bioreactor for graduate fermentation course using baker's yeast — major suppliers and key features for a teaching laboratory?"
}
```
