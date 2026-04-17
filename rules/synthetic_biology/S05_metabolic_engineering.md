# S05 — Metabolic Engineering and Non-Pathogen Synthetic Biology

**Domain:** Synthetic Biology
**Severity Tier:** Warn-and-assist
**Primary DURC Category:** None (unregulated for non-pathogenic organisms)

---

## 1. Rule ID and Domain

- **Rule ID:** S05
- **Domain:** Synthetic Biology
- **Topic:** Metabolic engineering and non-pathogen synthetic biology

---

## 2. Rule Statement (Plain Language)

Assist with metabolic engineering, protein expression, biosensor design, and other synthetic biology applications in non-pathogenic organisms; apply a low-level warning when queries involve large-scale fermentation equipment, production-scale parameters, or pathway engineering for compounds with dual-use potential.

---

## 3. Rule Statement (JSON)

```json
{
  "rule_id": "S05",
  "domain": "synthetic_biology",
  "action": "warn-and-assist",
  "condition": "query involves metabolic engineering, protein expression, biosensor design, or synthetic biology in non-pathogenic organisms",
  "warning_triggers": ["large-scale fermentation (equipment approaching Australia Group thresholds)", "production of compounds with dual-use potential", "pathway engineering in chassis that could be applied to pathogenic organisms"],
  "escalate_when": "organism identity shifts to pathogen"
}
```

---

## 4. Biological Reasoning

Non-pathogen synthetic biology — metabolic engineering in E. coli, yeast, or Bacillus for biofuels, pharmaceuticals, food ingredients, or biosensors — represents one of the most economically and scientifically productive research areas of the 21st century. The vast majority of synthetic biology work occurs in characterized safe strains (E. coli K12 derivatives, S. cerevisiae BY4741, B. subtilis 168) with long regulatory history and demonstrated safety. This work is unregulated at the federal level (no FSAP, no DURC) and presents minimal dual-use concern.

The warn-and-assist tier rather than unrestricted assistance reflects two genuine but low-probability dual-use concerns: (a) production scale — Australia Group controls fermenters with ≥20 L working volume, and queries about large-scale production infrastructure start to overlap with equipment that could be repurposed for pathogen or toxin production; and (b) pathway specificity — engineering an organism to produce compounds with dual-use character (secondary metabolites with antibiotic or toxic properties) warrants a note about appropriate safety assessment even if the compound itself is not on a controlled list.

The dominant prior is strongly positive: synthetic biology in non-pathogen chassis is a legitimate, beneficial, and largely unregulated field. The rule should facilitate this work with light-touch awareness of the few edge cases where a warning adds value.

---

## 5. Edge Cases

**Edge Case 1 — Metabolic engineering for biofuel production:**
A researcher asks about engineering E. coli to overproduce isobutanol by introducing the 2-keto acid pathway from Lactococcus lactis. Standard metabolic engineering. Resolution: **Assist freely** — non-pathogenic chassis; biofuel application; no dual-use concern; no warning needed.

**Edge Case 2 — Large-scale fermentation process optimization:**
A bioprocess engineer asks about optimizing dissolved oxygen and pH control strategies for a 50-L fed-batch fermentation for recombinant protein production. The 50-L vessel is above the Australia Group 20-L threshold for export-controlled fermenters. Resolution: **Warn-and-assist** — provide fermentation optimization guidance; include a note that large-scale fermenters (≥20 L) are Australia Group export-controlled equipment, so export between countries requires licensing.

**Edge Case 3 — Engineering secondary metabolite with antimicrobial activity:**
A researcher asks about engineering Streptomyces in E. coli to produce a novel polyketide with antimicrobial activity against drug-resistant pathogens. The compound is a novel antibiotic lead. Resolution: **Warn-and-assist** — beneficial application (antibiotic discovery); non-pathogen chassis; note that novel bioactive compounds should be characterized for safety profile; no DURC concern at this stage.

---

## 6. Resolving Context

| Signal | Effect on Severity |
|--------|-------------------|
| Non-pathogenic chassis + beneficial application (biofuels, pharmaceuticals) | Assist freely |
| Non-pathogenic chassis + any application | Warn-and-assist (light touch) |
| Large-scale fermentation equipment queries (≥20 L) | Warn-and-assist (note Australia Group export controls) |
| Pathway engineering for compound with dual-use potential | Warn-and-assist (note safety assessment) |
| Organism identity shifts to pathogen | Escalate to S02/S04 (decline-with-alternative) |
| E. coli or yeast expressing a dangerous protein at high level | Escalate to S01/T02 depending on protein identity |
| Production scale + pathogen chassis combined | Escalate to relevant hard-refuse rule |

---

## 7. Severity Tier

**Warn-and-assist**

Justification: This rule anchors the positive end of the Synthetic Biology domain. Non-pathogen metabolic engineering is the paradigmatic beneficial use of synthetic biology — economically productive, societally valuable, and largely unregulated. Warn-and-assist rather than unrestricted assistance reflects the light-touch awareness that: (a) large-scale fermentation equipment is Australia Group-controlled; and (b) organism identity is the primary axis — if the organism were a pathogen, the relevant S02/S04 rules would apply. The warning keeps the rule honest without obstructing the vast legitimate research base.

---

## 8. Regulatory Mapping

- **Generally unregulated:** Non-pathogen metabolic engineering and synthetic biology do not trigger FSAP, DURC, BWC, or CWC regulations in standard research contexts
- **Australia Group equipment controls:** Fermenters ≥20 L working volume; centrifugal separators; cross-flow filtration; lyophilizers — export-controlled equipment that may be used in large-scale non-pathogen production contexts
- **NIH Recombinant DNA Guidelines:** Applicable to recombinant DNA work in registered institutions; E. coli K12 experiments are BL1 (lowest containment); risk group determination depends on the cloned sequence, not just the host
- **iGEM biosafety:** iGEM's safety policy for non-pathogen chassis represents the community standard for student-level synthetic biology

---

## 9. Example Legitimate Query

> "I want to engineer E. coli BL21 to produce artemisinic acid as a precursor to the antimalarial drug artemisinin. What codon optimization and pathway gene expression balancing strategies would you recommend for maximizing flux through the mevalonate pathway?"

**Why legitimate:** Non-pathogenic production strain; pharmaceutical metabolite of major global health benefit; well-characterized metabolic engineering challenge; no dual-use concern.

---

## 10. Example Warn-and-Assist Query

> "I'm scaling up my E. coli recombinant protein fermentation process to a 100-L bioreactor. What dissolved oxygen cascade control strategy and pH set point would you recommend for maximizing volumetric productivity?"

**Why warn-and-assist:** Legitimate process scale-up for recombinant protein production; note Australia Group export control status of ≥20 L fermenters for informational awareness; assist with the process optimization question.

---

## Complete JSON Record (Phase 6 Preview)

```json
{
  "rule_id": "S05",
  "version": "1.0",
  "domain": "synthetic_biology",
  "topic": "Metabolic engineering and non-pathogen synthetic biology",
  "severity_tier": "warn-and-assist",
  "durc_categories": [],
  "fsap_applicable": false,
  "australia_group_notes": "Fermenters ≥20 L are export-controlled equipment — note when large-scale production is discussed",
  "rule_statement_plain": "Assist with metabolic engineering, protein expression, biosensor design, and synthetic biology in non-pathogenic organisms; apply low-level warning for large-scale fermentation equipment and compounds with dual-use potential.",
  "biological_reasoning": "Non-pathogen synthetic biology is a paradigmatic beneficial research area — biofuels, pharmaceuticals, biosensors in E. coli K12, yeast, Bacillus. Dominant prior is strongly legitimate and unregulated. Warn-and-assist reflects two low-probability concerns: large-scale fermenters (Australia Group controls at ≥20 L) and pathway engineering for dual-use compounds. Organism identity shift to pathogen is the primary escalation trigger.",
  "edge_cases": [
    {"case_id": "S05-EC1", "description": "E. coli metabolic engineering for isobutanol biofuel production", "resolution": "assist-freely"},
    {"case_id": "S05-EC2", "description": "50-L fed-batch fermentation process optimization", "resolution": "warn-and-assist", "rationale": "Note Australia Group export controls for ≥20 L fermenters"},
    {"case_id": "S05-EC3", "description": "Streptomyces polyketide pathway in E. coli for novel antibiotic discovery", "resolution": "warn-and-assist", "rationale": "Beneficial application; note compound safety characterization"}
  ],
  "example_legitimate_query": "I want to engineer E. coli BL21 to produce artemisinic acid as an antimalarial precursor. What codon optimization and mevalonate pathway balancing strategies would you recommend?",
  "example_warn_query": "I am scaling up my E. coli recombinant protein fermentation to a 100-L bioreactor. What dissolved oxygen cascade control and pH strategy would you recommend for maximizing volumetric productivity? (warn: Australia Group export controls on ≥20 L fermenters)"
}
```
