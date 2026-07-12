#!/usr/bin/env python3
"""Build a deterministic Hugging Face package from an exact Git commit."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


RELEASE_DATE = re.compile(r"^20[0-9]{2}-[0-9]{2}-[0-9]{2}$")
REPOSITORY = "jang1563/bio-constitution-rules"


class BuildError(RuntimeError):
    pass


def run_git(root: Path, *args: str, text: bool = True):
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip() if text else result.stdout


def git_blob(root: Path, commit: str, source_path: str) -> bytes:
    try:
        return run_git(root, "show", f"{commit}:{source_path}", text=False)
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise BuildError(f"cannot read {source_path} from {commit}: {detail}") from exc


def validate_source_commit(root: Path, commit: str) -> None:
    with tempfile.TemporaryDirectory(prefix="bio-constitution-source-") as temporary:
        worktree = Path(temporary) / "worktree"
        added = False
        try:
            subprocess.run(
                ["git", "worktree", "add", "--detach", "--quiet", str(worktree), commit],
                cwd=root,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            added = True
            result = subprocess.run(
                [sys.executable, str(worktree / "scripts/validate_release.py"), "--root", str(worktree)],
                cwd=worktree,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if result.returncode != 0:
                raise BuildError(
                    "selected source commit failed release validation:\n" + result.stdout[-6000:]
                )
        finally:
            if added:
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(worktree)],
                    cwd=root,
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )


def write_bytes(output: Path, relative: str, content: bytes) -> None:
    target = output / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)


def write_json(output: Path, relative: str, payload: dict) -> None:
    content = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    write_bytes(output, relative, content.encode("utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_records(output: Path, excluded: set[str] | None = None) -> list[dict]:
    excluded = excluded or set()
    records: list[dict] = []
    for path in sorted(item for item in output.rglob("*") if item.is_file()):
        relative = path.relative_to(output).as_posix()
        if relative in excluded:
            continue
        records.append(
            {"path": relative, "size": path.stat().st_size, "sha256": sha256(path)}
        )
    return records


def validate_package(output: Path) -> None:
    release_manifest = json.loads((output / "release_manifest.json").read_text())
    upload_manifest = json.loads((output / "upload_manifest.json").read_text())

    expected_upload = upload_manifest["files"]
    expected_paths = {record["path"] for record in expected_upload}
    actual_paths = set()
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(output).as_posix()
        if relative != "upload_manifest.json":
            actual_paths.add(relative)
    if expected_paths != actual_paths:
        raise BuildError(
            f"upload allowlist mismatch: missing={sorted(expected_paths - actual_paths)}, "
            f"extra={sorted(actual_paths - expected_paths)}"
        )

    for record in expected_upload:
        path = output / record["path"]
        if path.stat().st_size != record["size"] or sha256(path) != record["sha256"]:
            raise BuildError(f"hash/size mismatch for {record['path']}")

    payload_paths = {record["path"] for record in release_manifest["files"]}
    if "release_manifest.json" in payload_paths or "upload_manifest.json" in payload_paths:
        raise BuildError("release manifest must not include either manifest in its payload")
    for record in release_manifest["files"]:
        path = output / record["path"]
        if path.stat().st_size != record["size"] or sha256(path) != record["sha256"]:
            raise BuildError(f"release payload mismatch for {record['path']}")


def build(args: argparse.Namespace) -> Path:
    root = args.root.resolve()
    output = args.output_dir.resolve()
    if output == root or output.is_relative_to(root) or root.is_relative_to(output):
        raise BuildError("--output-dir must be outside and must not contain the source repository")
    if output.exists() and any(path.name == ".git" for path in output.rglob(".git")):
        raise BuildError("refusing to replace an output directory containing a Git repository")

    try:
        commit = run_git(root, "rev-parse", "--verify", f"{args.source_commit}^{{commit}}")
        tree = run_git(root, "rev-parse", f"{commit}^{{tree}}")
        tracked = set(run_git(root, "ls-tree", "-r", "--name-only", commit).splitlines())
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.decode("utf-8", errors="replace").strip()
        raise BuildError(f"cannot resolve source commit: {detail}") from exc

    required = {
        "LICENSE",
        "SAFETY.md",
        "data/dataset_stats.json",
        "data/training_dataset.jsonl",
        "docs/PROVENANCE.md",
        "docs/RELEASE_TRUST.md",
        "huggingface/.gitattributes",
        "huggingface/README.template.md",
        "release.json",
        "schema.json",
        "schemas/training-record.schema.json",
    }
    rule_paths = sorted(
        path for path in tracked if path.startswith("rules/") and path.endswith(".json")
    )
    if len(rule_paths) != 30:
        raise BuildError(f"expected 30 rule JSON files at source commit; got {len(rule_paths)}")
    missing = sorted(required - tracked)
    if missing:
        raise BuildError(f"source commit is missing package inputs: {missing}")

    validate_source_commit(root, commit)

    release_metadata = json.loads(git_blob(root, commit, "release.json"))
    release_date = release_metadata.get("release_date")
    if not isinstance(release_date, str) or not RELEASE_DATE.fullmatch(release_date):
        raise BuildError("release.json has an invalid release_date")
    if args.release_date is not None and args.release_date != release_date:
        raise BuildError("--release-date does not match the selected commit's release.json")

    if output.exists():
        if not args.force:
            raise BuildError(f"output exists: {output}; pass --force to replace it")
        shutil.rmtree(output)
    output.mkdir(parents=True)

    mappings = {
        "huggingface/.gitattributes": ".gitattributes",
        "LICENSE": "LICENSE",
        "SAFETY.md": "SAFETY.md",
        "data/training_dataset.jsonl": "data/train.jsonl",
        "data/dataset_stats.json": "data/dataset_stats.json",
        "schema.json": "schemas/rule.schema.json",
        "schemas/training-record.schema.json": "schemas/training-record.schema.json",
        "docs/PROVENANCE.md": "PROVENANCE.md",
        "docs/RELEASE_TRUST.md": "RELEASE_TRUST.md",
    }
    for source, destination in mappings.items():
        write_bytes(output, destination, git_blob(root, commit, source))
    for source in rule_paths:
        write_bytes(output, source, git_blob(root, commit, source))

    data_hash = sha256(output / "data/train.jsonl")
    template = git_blob(root, commit, "huggingface/README.template.md").decode("utf-8")
    replacements = {
        "{{SOURCE_COMMIT}}": commit,
        "{{SOURCE_TREE}}": tree,
        "{{DATA_SHA256}}": data_hash,
        "{{RELEASE_DATE}}": release_date,
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    unresolved = re.findall(r"\{\{[A-Z0-9_]+\}\}", template)
    if unresolved:
        raise BuildError(f"unresolved card placeholders: {sorted(set(unresolved))}")
    write_bytes(output, "README.md", template.encode("utf-8"))

    payload = file_records(output)
    write_json(
        output,
        "release_manifest.json",
        {
            "schema_version": 1,
            "repository": REPOSITORY,
            "release_date": release_date,
            "release_version": release_metadata.get("version"),
            "source_commit": commit,
            "source_tree": tree,
            "payload_file_count": len(payload),
            "files": payload,
        },
    )
    upload_files = file_records(output, excluded={"upload_manifest.json"})
    write_json(
        output,
        "upload_manifest.json",
        {
            "schema_version": 1,
            "repository": REPOSITORY,
            "source_commit": commit,
            "source_tree": tree,
            "file_count_excluding_self": len(upload_files),
            "files": upload_files,
        },
    )
    validate_package(output)
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--source-commit", required=True)
    parser.add_argument(
        "--release-date",
        help="optional assertion; must match release.json at the selected commit",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    try:
        output = build(args)
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"OK: built and verified Hugging Face package at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
