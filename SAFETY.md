# Safety and responsible use

Bio Constitution Rules is released for research on safety classification, rule authoring, and evaluation design. It is not a complete safeguard and must not be used as the sole control for a system that handles biological queries.

## Content scope

The repository contains decision criteria and synthetic user-query text. Some records name pathogens, toxins, regulated activities, or concerning research goals because those distinctions are necessary for evaluating a safety classifier. The release does not include experimental protocols, synthesis routes, dosing instructions, operational model responses, or step-by-step weaponization guidance.

## Known limitations

- Labels are derived from the published rules and have not been independently adjudicated.
- There are no human reviewer labels in version 1.0.0.
- The corpus is synthetic and English-centric; it is not sampled from production traffic.
- The 30-rule taxonomy is intentionally limited and cannot cover every biological context.
- Regulatory mappings are dated research annotations, not compliance determinations.
- Binary `ASSIST`/`REFUSE` collapse removes distinctions present in the five response tiers represented in the corpus.

## Appropriate use

- Inspecting and critiquing biosecurity rule taxonomies
- Developing annotation protocols and expert-review studies
- Testing data loaders, validation pipelines, or research classifiers
- Comparing multi-tier and binary decision representations

## Inappropriate use

- Treating the labels as expert ground truth
- Claiming deployment readiness from this dataset alone
- Using the rules as a substitute for institutional biosafety, legal, or regulatory review
- Reconstructing evasion guidance for a deployed safeguard

## Reporting sensitive concerns

Use the repository's GitHub Security Advisory flow for sensitive disclosures. Do not place operational biological details in a public issue. Ordinary data-quality corrections can use a public issue with the affected `query_id` or `rule_id` and a non-operational explanation.
