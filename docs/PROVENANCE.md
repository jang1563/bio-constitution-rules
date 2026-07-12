# Provenance

## Rule library

The release contains 30 JSON rule records across six domains. Legacy Markdown drafts are retained only in the private predecessor archive because they duplicated the JSON, contained stale policy language, and were not part of the validated machine-readable contract.

## Synthetic corpus

The 1,063-record corpus was assembled from rule-linked seed queries and synthetic paraphrases. The released JSONL contains 137 seed rows and 926 generated rows. Generated rows identify `claude-haiku-4-5-20251001` in the `generation_model` field because that value is part of the original data provenance; it is not a current model recommendation.

The labels were assigned by deterministic bio-specific and generic comparison rules. They were not collected from production traffic and were not independently adjudicated. All 1,063 `reviewer_label` values are null. The published JSON rules document the bio-specific rule IDs, but the original generic comparison rules and generation pipeline are outside this release, so `generic_label` cannot be regenerated from the public package alone.

## Curation boundary

Version 1.0.0 was curated into a fresh, parentless public Git root on 2026-07-13. The predecessor research history remains private. The public release intentionally excludes:

- application, interview, and internal handoff material
- local tool configuration and absolute filesystem paths
- raw per-query model responses and provider execution metadata
- fine-tuning run or model identifiers
- exploratory false-negative-rate outputs
- private review logs and unpublished research notes
- legacy rule Markdown and embedded preview records

The published data and rules were selected by explicit allowlist. See [RELEASE_TRUST.md](RELEASE_TRUST.md) for executable checks.

## Transformation notes

- The canonical public corpus is `data/training_dataset.jsonl`; the redundant JSON-array copy is not released.
- `data/dataset_stats.json` was regenerated from the canonical JSONL for the public release.
- Provider-specific language in general rule descriptions was rewritten to be provider-neutral. The `generation_model` data field remains unchanged for provenance.
- Regulatory metadata, incomplete strings, and obvious factual inconsistencies in the JSON rules were corrected during public curation without changing corpus rows, rule IDs, or response-tier labels.
- No row labels or query text were changed during public-surface curation.
