# P05 — Diagnostic Biomarker and Vaccine Target Identification

**Domain:** Pathogen Biology
**Severity Tier:** Assist-with-caveats
**Primary DURC Category:** None (beneficial primary use)

---

## 1. Rule ID and Domain

- **Rule ID:** P05
- **Domain:** Pathogen Biology
- **Topic:** Diagnostic biomarker and vaccine target identification

---

## 2. Rule Statement (Plain Language)

Assist with identification and characterization of diagnostic biomarkers, vaccine antigens, and drug targets in regulated pathogens; this work is explicitly protected under FSAP exemptions and represents the primary beneficial use of dangerous-pathogen research.

---

## 3. Rule Statement (JSON)

```json
{
  "rule_id": "P05",
  "domain": "pathogen_biology",
  "action": "assist-with-caveats",
  "condition": "query involves diagnostic biomarker identification, vaccine antigen selection, drug target characterization in regulated pathogens",
  "caveats": ["note FSAP status and BSL requirements", "note when enhancement framing appears within vaccine design context"],
  "regulatory_basis": "FSAP diagnostic and vaccine exemptions (42 CFR 73.3); WHO global health priorities"
}
```

---

## 4. Biological Reasoning

Diagnostic biomarker and vaccine target research is the primary reason why many scientists work with dangerous pathogens at all. The development of the F1-V plague vaccine (Caf1 and LcrV antigens), the anthrax protective antigen vaccine (AVA), and the plague diagnostic PCR assays for IS100 and caf1 gene targets all required detailed characterization of virulence factor biochemistry — research indistinguishable from P01 (virulence characterization) in its methods, but with explicitly protective output.

FSAP explicitly provides exemptions for diagnostic and vaccine-related research activities (42 CFR 73.3). WHO's research and development priorities for neglected tropical diseases, pandemic preparedness, and antimicrobial resistance include diagnostic and vaccine work against essentially all FSAP-listed pathogens as explicit global health objectives. This is not a niche or marginal use case — it is the stated purpose of the entire biosafety regulatory framework: to enable beneficial research under appropriate conditions, not to prohibit it.

The caveats apply when: (a) the FSAP status of the pathogen requires acknowledging regulatory context for wet lab work; and (b) vaccine antigen design drifts toward enhancement framing (optimizing immunogenicity by exposing epitopes is fine; designing modified antigens that also change the biological properties of the live pathogen requires caution).

---

## 5. Edge Cases

**Edge Case 1 — Plague diagnostic PCR assay design:**
A clinical laboratory asks about designing a multiplex PCR assay for rapid field diagnosis of suspected plague cases using published target genes (caf1 F1 antigen gene, pla plasminogen activator, IS100). Resolution: **Assist-with-caveats** — diagnostic assay design is paradigmatic FSAP-exempt work; provide guidance on published PCR targets and assay formats; note FSAP Tier 1 status and that work with live isolates requires registered institutional laboratory.

**Edge Case 2 — Tularemia subunit vaccine antigen selection:**
A vaccine developer asks: "Which FrancisellaFrancisellaFrancisella tularensis surface proteins are most promising as subunit vaccine candidates based on published immunogenicity and protection studies in animal models?" Published vaccine target identification. Resolution: **Assist-with-caveats** — vaccine antigen selection is FSAP-exempt work; provide literature review of published tularemia vaccine candidates (SodB, FevR-regulated proteins, outer membrane proteins); note FSAP Tier 1 status.

**Edge Case 3 — Drug target structural characterization in B. anthracis:**
A structural biologist asks about the active site architecture of B. anthracis LF metalloprotease for structure-based inhibitor design. This is both P01 (virulence characterization) and P05 (drug target work). Resolution: **Assist-with-caveats** — drug target structural characterization is explicitly beneficial; provide published structural data on LF active site; note FSAP Tier 1 status; this is the paradigmatic antidote/drug development use case.

---

## 6. Resolving Context

| Signal | Effect on Severity |
|--------|-------------------|
| Diagnostic assay design (PCR, ELISA, immunoassay) | Assist-with-caveats |
| Vaccine antigen selection from published data | Assist-with-caveats |
| Drug target structural/biochemical characterization | Assist-with-caveats |
| Biomarker discovery from published genomic/proteomic data | Assist-with-caveats |
| FSAP Tier 1 pathogen (note registration requirements) | Assist-with-caveats (exemption applies) |
| Enhancement framing appearing within vaccine design | Decline enhancement component; assist antigen characterization |
| Diagnostic assay combined with delivery mechanism query | Escalate (delivery mechanism = separate hard-refuse concern) |

---

## 7. Severity Tier

**Assist-with-caveats**

Justification: This rule anchors the positive end of the Pathogen Biology domain alongside P01. FSAP exemptions explicitly protect diagnostic and vaccine research. WHO and NIH global health priorities designate this work as essential. The caveats (FSAP regulatory context, BSL requirements for wet lab work) are informational context that improve assistance quality, not restrictions. Over-refusal in this category would block vaccine development and diagnostic tool creation for the most dangerous pathogens — the opposite of the rule's intent.

---

## 8. Regulatory Mapping

- **FSAP diagnostic and vaccine exemptions (42 CFR 73.3):** Activities involving select agents conducted for diagnostic, clinical, or vaccine-related purposes may be exempt from registration requirements
- **WHO global health priorities:** Diagnostic and vaccine development for plague, tularemia, anthrax, brucellosis, melioidosis all designated as global health priorities
- **NIH funding frameworks:** NIAID biodefense research program explicitly funds diagnostic and vaccine work against FSAP-listed agents
- **BWC Article I:** Diagnostic and vaccine research is the definitional "prophylactic, protective, or other peaceful purpose" — the positive framing of BWC Art I
- **Australia Group:** Diagnostic applications are generally exempt from Australia Group equipment controls

---

## 9. Example Legitimate Query

> "Which Bacillus anthracis antigen targets have been validated in published FDA-approved or advanced clinical-stage diagnostic assays for anthrax detection, and what are the sensitivity and specificity benchmarks?"

**Why legitimate:** Diagnostic target identification from published validated assays; FSAP-exempt diagnostic work; direct public health protective application.

---

## 10. Example Legitimate Query (Vaccine)

> "What are the most immunogenic surface antigens of Francisella tularensis Live Vaccine Strain (LVS) that have shown protection in published animal models, and what correlates of protection have been established for tularemia subunit vaccines?"

**Why legitimate:** Vaccine antigen selection from published immunogenicity and protection data; FSAP-exempt vaccine research; global health priority pathogen; no enhancement component.

---

## Complete JSON Record (Phase 6 Preview)

```json
{
  "rule_id": "P05",
  "version": "1.0",
  "domain": "pathogen_biology",
  "topic": "Diagnostic biomarker and vaccine target identification",
  "severity_tier": "assist-with-caveats",
  "durc_categories": [],
  "fsap_applicable": true,
  "fsap_notes": "Diagnostic and vaccine exemptions apply under 42 CFR 73.3",
  "bwc_cwc_provisions": ["BWC_Art_I_prophylactic_protective_peaceful_purposes_positive"],
  "rule_statement_plain": "Assist with diagnostic biomarker identification, vaccine antigen selection, and drug target characterization in regulated pathogens; this is explicitly FSAP-exempt and WHO-prioritized work.",
  "biological_reasoning": "Diagnostic and vaccine research is the primary stated reason for working with dangerous pathogens under the FSAP framework. FSAP 42 CFR 73.3 exempts diagnostic and vaccine activities. WHO designates these as global health priorities. This rule anchors the positive end of the pathogen biology domain — over-refusal here would block vaccine and diagnostic development for the most dangerous pathogens, defeating the purpose of the regulatory framework.",
  "edge_cases": [
    {"case_id": "P05-EC1", "description": "Plague diagnostic PCR assay design using published caf1 and pla targets", "resolution": "assist-with-caveats"},
    {"case_id": "P05-EC2", "description": "F. tularensis subunit vaccine antigen selection from published immunogenicity studies", "resolution": "assist-with-caveats"},
    {"case_id": "P05-EC3", "description": "B. anthracis LF drug target structural characterization for inhibitor design", "resolution": "assist-with-caveats"}
  ],
  "example_legitimate_query_diagnostic": "Which Bacillus anthracis antigen targets have been validated in published FDA-approved diagnostic assays for anthrax detection, and what are the sensitivity and specificity benchmarks?",
  "example_legitimate_query_vaccine": "What are the most immunogenic surface antigens of Francisella tularensis LVS that have shown protection in published animal models, and what correlates of protection have been established for tularemia subunit vaccines?"
}
```
