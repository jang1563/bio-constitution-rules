# Release trust report

## Public allowlist

The public surface is limited to:

- project, contribution, security, safety, citation, license, and changelog documents
- 30 JSON rules; legacy Markdown companions are explicitly excluded
- the rule schema and training-record schema
- one canonical 1,063-record JSONL corpus and its recomputable statistics
- validation, release-manifest, and Hugging Face package tooling
- pinned GitHub Actions workflow configuration

## Explicit exclusions

The validator fails if tracked paths contain internal handoffs, local assistant configuration, private research folders, reviewer logs, raw model result directories, or fine-tuning result artifacts. It also scans tracked text for common secret formats and absolute local paths.

## Reproducible checks

Run these commands from a checkout of the linked GitHub source repository; the Hugging Face mirror contains the release payload and manifests, not the build scripts.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_release.py
```

The validator checks:

- the exact tracked-file allowlist, including all nested paths
- 30 unique rules, five per domain, against `schema.json`
- no tracked rule Markdown and exactly 30 schema-valid JSON rules
- current policy-basis and non-compliance disclaimer fields on every rule
- rejection of legacy `Tier 2`, old DURC category fields, and truncated rule reasoning
- 1,063 parseable JSONL rows with unique IDs and query text
- every dataset `rule_id` and domain linked to the public rule library
- zero non-null human reviewer labels
- recomputed statistics against `data/dataset_stats.json`
- forbidden paths, local paths, direct email addresses, and key-like strings
- the presence of deterministic Hugging Face package placeholders

The Hugging Face builder first checks the selected commit in a temporary detached worktree, then reads every payload from that Git commit object rather than from uncommitted working-tree files. Its manifests record the exact source commit, source tree, path allowlist, sizes, and SHA-256 values. `release_manifest.json` hashes the payload; `upload_manifest.json` additionally hashes `release_manifest.json` and intentionally does not self-hash. The output directory must be outside the source repository; `--force` refuses to remove a directory that contains a Git repository.

## Claim boundary

This release does not publish a model benchmark as a release claim. Earlier exploratory pilot, cross-validation, adversarial, fine-tuning, and false-negative-rate outputs are outside the public package because they were not independently replicated and some contained provider-specific execution metadata.
