#!/usr/bin/env python3
"""Fail-closed validation for the public Bio Constitution Rules release."""

from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator


EXPECTED_STATIC_FILES = {
    ".github/workflows/validate-release.yml",
    ".gitignore",
    "CHANGELOG.md",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SAFETY.md",
    "SECURITY.md",
    "data/dataset_stats.json",
    "data/training_dataset.jsonl",
    "docs/PROVENANCE.md",
    "docs/REGULATORY_SNAPSHOT.md",
    "docs/RELEASE_TRUST.md",
    "huggingface/.gitattributes",
    "huggingface/README.template.md",
    "requirements-dev.txt",
    "release.json",
    "schema.json",
    "schemas/training-record.schema.json",
    "scripts/build_hf_release_package.py",
    "scripts/validate_release.py",
}

EXPECTED_RULE_FILES = {
    "rules/dual_use_chemistry/C01_schedule1_synthesis.json",
    "rules/dual_use_chemistry/C02_precursor_sourcing.json",
    "rules/dual_use_chemistry/C03_ai_molecular_design.json",
    "rules/dual_use_chemistry/C04_delivery_system.json",
    "rules/dual_use_chemistry/C05_reagent_sourcing.json",
    "rules/genomics/G01_functional_annotation.json",
    "rules/genomics/G02_ai_sequence_design.json",
    "rules/genomics/G03_pandemic_potential.json",
    "rules/genomics/G04_variant_effect_prediction.json",
    "rules/genomics/G05_metagenomics.json",
    "rules/pathogen_biology/P01_virulence_characterization.json",
    "rules/pathogen_biology/P02_virulence_engineering.json",
    "rules/pathogen_biology/P03_amr_resistance.json",
    "rules/pathogen_biology/P04_immune_evasion_bacterial.json",
    "rules/pathogen_biology/P05_diagnostic_vaccine_targets.json",
    "rules/synthetic_biology/S01_de_novo_synthesis.json",
    "rules/synthetic_biology/S02_genetic_circuit_design.json",
    "rules/synthetic_biology/S03_directed_evolution.json",
    "rules/synthetic_biology/S04_crispr_editing.json",
    "rules/synthetic_biology/S05_metabolic_engineering.json",
    "rules/toxicology/T01_mechanism_of_action.json",
    "rules/toxicology/T02_SAR_lethality.json",
    "rules/toxicology/T03_production_scale_up.json",
    "rules/toxicology/T04_delivery_dispersal.json",
    "rules/toxicology/T05_antidote_countermeasure.json",
    "rules/virology/V01_airborne_transmission.json",
    "rules/virology/V02_host_range.json",
    "rules/virology/V03_immune_evasion.json",
    "rules/virology/V04_extinct_virus_reconstitution.json",
    "rules/virology/V05_vaccine_antigen_design.json",
}

EXPECTED_TRACKED_FILES = EXPECTED_STATIC_FILES | EXPECTED_RULE_FILES

FORBIDDEN_PATH_PARTS = {
    ".claude",
    "application_materials",
    "finetune_results",
    "fnr_results",
    "handoff",
    "handoffs",
    "phase10",
    "phase11",
    "research",
    "reviewer_log.md",
}

TEXT_SCAN_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    "Hugging Face token": re.compile(r"\bhf_[A-Za-z0-9]{16,}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{16,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "absolute user path": re.compile(
        r"(?:/" + r"Users/|/" + r"home/|[A-Za-z]:\\\\" + r"Users\\\\)"
    ),
    "direct email address": re.compile(
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE
    ),
}

EXPECTED_DOMAINS = {
    "dual_use_chemistry",
    "genomics",
    "pathogen_biology",
    "synthetic_biology",
    "toxicology",
    "virology",
}


class ReleaseError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ReleaseError(message)


def git_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {path}: {exc}")


def materialize_index(root: Path) -> tuple[Path, tempfile.TemporaryDirectory]:
    holder = tempfile.TemporaryDirectory(prefix="bio-constitution-release-index-")
    snapshot = Path(holder.name)
    subprocess.run(
        ["git", "checkout-index", "--all", f"--prefix={snapshot.as_posix()}/"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return snapshot, holder


def validate_boundary(tracked: list[str]) -> None:
    if not tracked:
        fail("Git index is empty; stage the intended release files before validation")

    tracked_set = set(tracked)
    if tracked_set != EXPECTED_TRACKED_FILES:
        missing = sorted(EXPECTED_TRACKED_FILES - tracked_set)
        extra = sorted(tracked_set - EXPECTED_TRACKED_FILES)
        fail(f"exact tracked-file boundary mismatch; missing={missing}, extra={extra}")

    for path in tracked:
        lowered_parts = {part.lower() for part in Path(path).parts}
        hit = lowered_parts & FORBIDDEN_PATH_PARTS
        if hit:
            fail(f"forbidden public path {path}: {sorted(hit)}")


def validate_text_surface(root: Path, tracked: list[str]) -> None:
    findings: list[str] = []
    for relative in tracked:
        path = root / relative
        try:
            raw = path.read_bytes()
        except OSError as exc:
            fail(f"cannot read tracked file {relative}: {exc}")
        if b"\0" in raw:
            continue
        text = raw.decode("utf-8", errors="replace")
        for label, pattern in TEXT_SCAN_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{relative}: {label}")
    if findings:
        fail("public text-surface scan failed:\n  " + "\n  ".join(findings))


def validate_rules(root: Path) -> None:
    schema = load_json(root / "schema.json")
    validator = Draft202012Validator(schema)
    json_paths = sorted((root / "rules").glob("*/*.json"))
    markdown_paths = sorted((root / "rules").glob("*/*.md"))

    if len(json_paths) != 30:
        fail(f"expected exactly 30 JSON rules; got {len(json_paths)}")
    if markdown_paths:
        fail("legacy rule Markdown must remain outside the public release")

    rule_ids: set[str] = set()
    domain_counts: collections.Counter[str] = collections.Counter()
    errors: list[str] = []
    forbidden_keys = {
        "durc_categories",
        "fsap_applicable",
        "fsap_thresholds",
        "iasb_screening_protocol",
    }
    for path in json_paths:
        record = load_json(path)
        for error in validator.iter_errors(record):
            location = "/".join(map(str, error.absolute_path)) or "<root>"
            errors.append(f"{path.relative_to(root)}:{location}: {error.message}")
        rule_id = record.get("rule_id")
        if rule_id in rule_ids:
            errors.append(f"duplicate rule_id {rule_id}")
        rule_ids.add(rule_id)
        domain_counts[record.get("domain")] += 1
        if not path.name.startswith(f"{rule_id}_"):
            errors.append(f"filename does not match rule_id: {path.relative_to(root)}")
        legacy_keys = sorted(forbidden_keys & set(record))
        if legacy_keys:
            errors.append(f"{path.relative_to(root)} uses legacy keys: {legacy_keys}")
        if re.search(r"\btier[ -]?2\b", json.dumps(record), re.IGNORECASE):
            errors.append(f"{path.relative_to(root)} uses nonexistent FSAP Tier 2 terminology")
        reasoning = record.get("biological_reasoning", "").strip()
        if reasoning and reasoning[-1] not in ".!?)]":
            errors.append(f"{path.relative_to(root)} biological_reasoning appears truncated")

    if errors:
        fail("rule validation failed:\n  " + "\n  ".join(errors[:30]))
    if set(domain_counts) != EXPECTED_DOMAINS or any(
        domain_counts[domain] != 5 for domain in EXPECTED_DOMAINS
    ):
        fail(f"expected five rules in each domain; got {dict(domain_counts)}")


def load_rows(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSONL at {path}:{line_number}: {exc}")
        if not isinstance(record, dict):
            fail(f"expected object at {path}:{line_number}")
        rows.append(record)
    return rows


def computed_stats(rows: list[dict]) -> dict:
    domain_distribution: dict[str, dict[str, int]] = {}
    for domain in sorted(EXPECTED_DOMAINS):
        domain_rows = [row for row in rows if row["domain"] == domain]
        divergence_types = collections.Counter(row["divergence_type"] for row in domain_rows)
        domain_distribution[domain] = {
            "total": len(domain_rows),
            "AGREE": divergence_types["AGREE"],
            "FN": divergence_types["FN"],
            "FP": divergence_types["FP"],
        }

    divergence_types = collections.Counter(row["divergence_type"] for row in rows)
    bio_labels = collections.Counter(row["bio_collapsed"] for row in rows)
    generic_labels = collections.Counter(row["generic_label"] for row in rows)
    query_types = collections.Counter(row["query_type"] for row in rows)
    review_status = collections.Counter(row["review_status"] for row in rows)
    divergence_records = sum(bool(row["divergence"]) for row in rows)

    return {
        "release_version": "1.0.0",
        "record_count": len(rows),
        "unique_query_ids": len({row["query_id"] for row in rows}),
        "unique_query_texts": len({row["query_text"] for row in rows}),
        "seed_records": sum(bool(row["is_seed"]) for row in rows),
        "generated_records": sum(not bool(row["is_seed"]) for row in rows),
        "human_reviewed_records": sum(row["reviewer_label"] is not None for row in rows),
        "pending_expert_review_records": review_status["pending"],
        "pipeline_not_required_records": review_status["not_required"],
        "divergence_records": divergence_records,
        "divergence_rate": round(divergence_records / len(rows), 6),
        "divergence_type_distribution": {
            key: divergence_types[key] for key in ("AGREE", "FN", "FP")
        },
        "bio_collapsed_distribution": {key: bio_labels[key] for key in ("ASSIST", "REFUSE")},
        "generic_label_distribution": {
            key: generic_labels[key] for key in ("ASSIST", "REFUSE")
        },
        "query_type_distribution": {key: query_types[key] for key in ("A", "B", "C")},
        "domain_distribution": domain_distribution,
    }


def validate_dataset(root: Path) -> None:
    rows = load_rows(root / "data/training_dataset.jsonl")
    if len(rows) != 1063:
        fail(f"expected 1,063 training rows; got {len(rows)}")

    public_rules = {
        record["rule_id"]: record
        for record in (
            load_json(path) for path in sorted((root / "rules").glob("*/*.json"))
        )
    }
    schema = load_json(root / "schemas/training-record.schema.json")
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    for index, row in enumerate(rows, 1):
        for error in validator.iter_errors(row):
            location = "/".join(map(str, error.absolute_path)) or "<root>"
            errors.append(f"row {index}:{location}: {error.message}")
            if len(errors) >= 30:
                break
        expected_divergence = row["bio_collapsed"] != row["generic_label"]
        if row["divergence"] != expected_divergence:
            errors.append(f"row {index}: divergence flag is inconsistent")
        expected_type = (
            "AGREE"
            if not expected_divergence
            else "FN"
            if row["bio_collapsed"] == "REFUSE"
            else "FP"
        )
        if row["divergence_type"] != expected_type:
            errors.append(f"row {index}: divergence_type should be {expected_type}")
        if row["bio_rule_fired"] != row["rule_id"]:
            errors.append(f"row {index}: bio_rule_fired does not match rule_id")
        rule = public_rules.get(row["rule_id"])
        if rule is None:
            errors.append(f"row {index}: rule_id is absent from the public rule library")
        elif row["domain"] != rule["domain"]:
            errors.append(f"row {index}: domain does not match its public rule")
        if row["bio_label"] != row["severity_tier"]:
            errors.append(f"row {index}: bio_label does not match severity_tier")
        if row["is_ambiguous"]:
            errors.append(f"row {index}: ambiguous rows must not be in the training split")
        if errors and len(errors) >= 30:
            break

    if errors:
        fail("training dataset validation failed:\n  " + "\n  ".join(errors))

    if len({row["query_id"] for row in rows}) != len(rows):
        fail("query_id values are not unique")
    if len({row["query_text"] for row in rows}) != len(rows):
        fail("query_text values are not unique")
    if any(row["reviewer_label"] is not None or row["reviewer_notes"] is not None for row in rows):
        fail("release claims zero human labels but non-null reviewer fields were found")

    expected = load_json(root / "data/dataset_stats.json")
    actual = computed_stats(rows)
    if actual != expected:
        fail(
            "dataset statistics are stale\n"
            f"expected={json.dumps(expected, sort_keys=True)}\n"
            f"actual={json.dumps(actual, sort_keys=True)}"
        )


def validate_hf_template(root: Path) -> None:
    template = (root / "huggingface/README.template.md").read_text(encoding="utf-8")
    required = {
        "{{SOURCE_COMMIT}}",
        "{{SOURCE_TREE}}",
        "{{DATA_SHA256}}",
        "{{RELEASE_DATE}}",
    }
    missing = sorted(token for token in required if token not in template)
    if missing:
        fail(f"Hugging Face card template is missing placeholders: {missing}")


def validate_release_metadata(root: Path) -> None:
    metadata = load_json(root / "release.json")
    if metadata != {"version": "1.0.0", "release_date": "2026-07-13"}:
        fail(f"unexpected release metadata: {metadata}")
    if load_json(root / "data/dataset_stats.json")["release_version"] != metadata["version"]:
        fail("dataset release_version does not match release.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: script parent)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    try:
        tracked = git_files(root)
        snapshot, holder = materialize_index(root)
        try:
            validate_boundary(tracked)
            validate_text_surface(snapshot, tracked)
            validate_rules(snapshot)
            validate_dataset(snapshot)
            validate_hf_template(snapshot)
            validate_release_metadata(snapshot)
        finally:
            holder.cleanup()
    except (ReleaseError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("OK: public release boundary")
    print("OK: 30 JSON-only rule records with current policy metadata")
    print("OK: 1,063 unique synthetic records; 0 human reviewer labels")
    print("OK: statistics, text-surface scan, and Hugging Face template")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
