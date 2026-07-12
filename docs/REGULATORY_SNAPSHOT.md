# Regulatory annotation snapshot

Targeted fields were checked against official public sources on 2026-07-13. This was not a complete expert or legal review of every biological judgment in the rule set.

The rule records contain fields such as `risk_outcome_tags`, `fsap_context_relevant`, `fsap_agents`, legacy policy references, and treaty or control-list references. These values are internal research annotations. They are not legal advice or an institutional biosafety determination.

## United States research-oversight policy

The policy surface changed after the original annotations were drafted. Executive Order 14292, issued 2025-05-05, directed the Office of Science and Technology Policy to revise or replace the 2024 U.S. Government DURC/PEPP policy. NIH subsequently stated that covered dangerous gain-of-function work would be terminated or suspended pending implementation of the new policy. Version 1.0.0 therefore uses provider-neutral `risk_outcome_tags` aligned to the outcome letters in Section 8 of the Executive Order. These tags are an internal retrieval taxonomy, not a determination that a project is legally covered.

Primary sources:

- [Executive Order 14292: Improving the Safety and Security of Biological Research](https://www.whitehouse.gov/presidential-actions/2025/05/improving-the-safety-and-security-of-biological-research/)
- [NIH NOT-OD-25-127 implementation update](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-127.html)

## Federal Select Agent Program

FSAP annotations are research aids only. Version 1.0.0 corrected Tier 1 status against the current list, removed the nonexistent `Tier 2` label, reflected the 2025 Brucella and Nipah changes, and updated permissible toxin amounts. Case-specific status must still be checked directly in the regulations and current agency guidance.

Primary sources:

- [Federal Select Agent Program regulations](https://www.selectagents.gov/regulations/index.htm)
- [Current Select Agents and Toxins list](https://www.selectagents.gov/sat/list.htm)
- [Current permissible toxin amounts](https://www.selectagents.gov/sat/permissible.htm)
- [2025 list-change notice](https://www.selectagents.gov/resources/sagrams/2025.htm)

## International frameworks

WHO risk-group, BWC, CWC, Australia Group, and synthesis-screening references likewise require case-specific and date-specific verification. The CWC Schedule 1 annotations in version 1.0.0 were limited to the relevant listed toxins, ricin and saxitoxin. These fields make the rule-authoring rationale inspectable; they do not provide a compliance service.

- [OPCW Chemical Weapons Convention Schedule 1](https://www.opcw.org/chemical-weapons-convention/annexes/annex-chemicals/schedule-1)

## Recommended use

Treat each regulatory field as a hypothesis or retrieval key for expert review. Before operational use, attach a verification date, primary-source link, jurisdiction, and reviewer identity to every relied-upon mapping.
