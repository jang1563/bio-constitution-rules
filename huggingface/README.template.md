---
license: apache-2.0
language:
  - en
task_categories:
  - text-classification
pretty_name: Bio Constitution Rules
size_categories:
  - 1K<n<10K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
---

# Bio Constitution Rules

A research dataset containing 30 machine-readable biological dual-use decision rules and 1,063 synthetic, rule-derived text-classification records.

## Important label boundary

- These labels are synthetic targets derived from the published rules; they are not expert-validated ground truth.
- Human reviewer labels: **0 / 1,063**.
- The 418 `pending` rows are candidates for future expert review. `not_required` is pipeline bookkeeping only.
- This dataset is not a production safeguard and carries no model-accuracy or deployment-readiness claim.
- Regulatory fields are dated research annotations, not legal or institutional compliance determinations.

## Data files

```python
from datasets import load_dataset

dataset = load_dataset("jang1563/bio-constitution-rules", split="train")
print(dataset.num_rows)  # 1063
```

The canonical split is `data/train.jsonl`. Rules are available as JSON under `rules/`. The schemas and recomputed aggregate statistics are included in the package.

## Core fields

| Field | Meaning |
|---|---|
| `query_id` | Unique synthetic record identifier |
| `rule_id` | Bio-specific rule associated with the row |
| `query_text` | Seed or synthetic query text |
| `bio_label` | Full rule-derived response tier |
| `bio_collapsed` | Binary `ASSIST` or `REFUSE` projection |
| `generic_label` | Deterministic generic-rule comparison label |
| `divergence_type` | `AGREE`, generic false positive (`FP`), or generic false negative (`FN`) relative to the bio rule |
| `review_status` | Pipeline bookkeeping; not evidence of human review |
| `reviewer_label` | Always null in version 1.0.0 |

The complete 25-field contract is in `schemas/training-record.schema.json`.

The original generic comparison rules and generation pipeline are outside this public package. `generic_label` is retained as provenance-bearing data but cannot be independently regenerated from the mirror alone.

## Safety and limitations

The records include non-operational descriptions of concerning biological goals because the dataset is intended for safety-classification research. The package excludes raw model responses, experimental protocols, provider execution metadata, and fine-tuning identifiers. Read `SAFETY.md` and `PROVENANCE.md` before use.

## Provenance and integrity

- Release date: `{{RELEASE_DATE}}`
- Git source commit: `{{SOURCE_COMMIT}}`
- Git source tree: `{{SOURCE_TREE}}`
- `data/train.jsonl` SHA-256: `{{DATA_SHA256}}`

`release_manifest.json` hashes the release payload. `upload_manifest.json` provides the upload allowlist and additionally hashes the release manifest; as the outermost inventory, it intentionally does not hash itself.

## License

Apache License 2.0.
