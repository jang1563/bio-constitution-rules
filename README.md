# Bio Constitution Rules

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Release validation](https://github.com/jang1563/bio-constitution-rules/actions/workflows/validate-release.yml/badge.svg)](https://github.com/jang1563/bio-constitution-rules/actions/workflows/validate-release.yml)
[![Hugging Face](https://img.shields.io/badge/dataset-Hugging%20Face-yellow)](https://huggingface.co/datasets/jang1563/bio-constitution-rules)

A research dataset of 30 machine-readable decision rules for biological dual-use content, accompanied by a 1,063-record synthetic text-classification corpus.

## Release boundary

This repository is a research prototype, not a production safeguard or a regulatory decision system.

- The 1,063 labels are rule-derived synthetic targets. They are not expert-validated ground truth.
- No released record has a human reviewer label. The 418 `pending` rows are candidates for future expert review; `not_required` is pipeline bookkeeping, not evidence of review.
- The release makes no model-accuracy, deployment-readiness, or independent-validation claim.
- Regulatory fields are dated research annotations. They are not legal advice and may not reflect the current policy applicable to a particular institution or project.
- Raw model responses, provider run metadata, fine-tuning identifiers, internal handoffs, and application materials are outside the public boundary.

See [SAFETY.md](SAFETY.md), [docs/PROVENANCE.md](docs/PROVENANCE.md), and [docs/REGULATORY_SNAPSHOT.md](docs/REGULATORY_SNAPSHOT.md) before using the data.

## Contents

| Artifact | Count | Purpose |
|---|---:|---|
| JSON rules | 30 | Machine-readable rule records across six domains |
| Synthetic records | 1,063 | Rule-derived classification examples in JSONL |
| Human-reviewed records | 0 | Expert review remains future work |

The six domains are virology, toxicology, synthetic biology, genomics, pathogen biology, and dual-use chemistry. Each domain contains five rules.

## Quick start

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_release.py
```

Load the training records:

```python
import json
from pathlib import Path

rows = [
    json.loads(line)
    for line in Path("data/training_dataset.jsonl").read_text().splitlines()
    if line.strip()
]

print(len(rows))                 # 1063
print(rows[0]["bio_collapsed"]) # REFUSE or ASSIST
```

Inspect a rule:

```python
import json

with open("rules/virology/V01_airborne_transmission.json") as handle:
    rule = json.load(handle)

print(rule["rule_id"], rule["severity_tier"])
```

## Label semantics

`bio_label` is the full rule-derived response tier. `bio_collapsed` maps that tier to `ASSIST` or `REFUSE` for binary experiments. `generic_label` is a deterministic comparison label from the original generic-rule baseline. None of these fields is a human annotation.

`divergence=true` means the bio-specific and generic deterministic rules disagree. It does not mean either label has been independently adjudicated.

The original generic comparison rules and generation pipeline are not part of this release, so `generic_label` is provenance-bearing data but is not independently regenerable from the public package alone.

The public statistics in [data/dataset_stats.json](data/dataset_stats.json) are recomputed and checked by the release validator.

## Repository layout

```text
.
├── data/                         # canonical JSONL and recomputable statistics
├── docs/                         # provenance, policy snapshot, release trust notes
├── huggingface/                  # deterministic dataset-card template
├── rules/                        # 30 JSON rules; legacy Markdown drafts excluded
├── schemas/                      # training-record schema
├── scripts/                      # release and Hugging Face validators/builders
├── schema.json                   # rule schema
├── SAFETY.md
└── SECURITY.md
```

## Hugging Face release

The Hugging Face package is built from an exact Git commit rather than from the mutable working tree:

```bash
python3 scripts/build_hf_release_package.py \
  --source-commit HEAD \
  --output-dir /tmp/bio-constitution-rules-hf
```

The builder emits `release_manifest.json` and `upload_manifest.json` with the source commit, source tree, file allowlist, sizes, and SHA-256 hashes.

## Citation

Citation metadata is available in [CITATION.cff](CITATION.cff).

## License

Apache License 2.0. See [LICENSE](LICENSE).
