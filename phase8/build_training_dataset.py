"""
Phase 8 Step 5: Merge bio and generic labels, compute divergence, produce final datasets.

Reads:  phase8/paraphrases_bio_labeled.json  (bio labels)
        phase8/paraphrases_generic_labeled.json  (generic labels)
        phase8/seeds.json  (for seed_query_text lookup in divergence records)
        phase8/generation_stats_tmp.json  (generation metadata)
        phase7/pilot_test_set.json  (for pilot_analog lookup)

Writes:
  training_dataset.json   — all non-ambiguous labeled records
  training_dataset.jsonl  — same, JSONL format
  divergence_set.json     — FP and FN records enriched with divergence metadata
  ambiguous_set.json      — records from ambiguous seeds
  dataset_stats.json      — aggregate metrics
"""

import json
import pathlib
from datetime import date

PHASE8 = pathlib.Path(__file__).parent
PHASE7 = PHASE8.parent / "phase7"

BIO_FILE = PHASE8 / "paraphrases_bio_labeled.json"
GENERIC_FILE = PHASE8 / "paraphrases_generic_labeled.json"
SEEDS_FILE = PHASE8 / "seeds.json"
PILOT_FILE = PHASE7 / "pilot_test_set.json"
GEN_STATS_FILE = PHASE8 / "generation_stats_tmp.json"

# Divergence category lookup by rule_id
DIVERGENCE_CATEGORY = {
    "T01": "mechanism_vs_synthesis",
    "T02": "mechanism_vs_synthesis",
    "C01": "mechanism_vs_synthesis",
    "C02": "precursor_combination_logic",
    "C03": "therapeutic_context",
    "C04": "weaponization_vs_industrial",
    "V01": "retrospective_vs_prospective",
    "V04": "retrospective_vs_prospective",
    "G03": "retrospective_vs_prospective",
    "P03": "amr_surveillance_vs_engineering",
    "P04": "immune_evasion_characterization",
    "S01": "antigen_vs_genome_synthesis",
    "G04": "clinical_vs_enhancement_vep",
    "G01": "annotation_vs_enhancement",
    "V03": "framing_invariance",
    "S03": "framing_invariance",
    "G02": "framing_invariance",
    "P02": "embedded_escalation",
    "T05": "embedded_escalation",
    "V02": "host_range_characterization",
    "S02": "chassis_organism_identity",
    "S04": "crispr_pathogen_vs_lab_strain",
    "G05": "metagenomics_vs_isolation",
    "P01": "characterization_vs_enhancement_boundary",
    "P05": "diagnostic_vaccine_target",
    "V05": "vaccine_antigen_standard",
    "T03": "quantity_threshold_logic",
    "T04": "delivery_weaponization",
    "S05": "metabolic_engineering_legitimate",
    "C05": "reagent_sourcing_legitimate",
}


def build_pilot_analog_map(pilot_file: pathlib.Path) -> dict[str, str]:
    """Build {rule_id -> pilot_query_id} for known divergence cases."""
    if not pilot_file.exists():
        return {}
    pilot = json.loads(pilot_file.read_text())
    analog_map = {}
    for q in pilot.get("queries", []):
        if q.get("divergence"):
            rule = q.get("rule_fired", "")
            if rule and rule not in analog_map:
                analog_map[rule] = q["query_id"]
    return analog_map


def gate4_global_duplicate(records: list[dict]) -> list[dict]:
    """Remove exact duplicate query_texts (case-insensitive, strip whitespace)."""
    seen = set()
    out = []
    for rec in records:
        key = rec["query_text"].strip().lower()
        if key not in seen:
            seen.add(key)
            out.append(rec)
    return out


def compute_divergence(bio_collapsed: str, generic_label: str) -> tuple[bool, str]:
    if bio_collapsed in ("AMBIGUOUS",):
        return False, "AMBIGUOUS"
    if bio_collapsed == generic_label:
        return False, "AGREE"
    if bio_collapsed == "ASSIST" and generic_label == "REFUSE":
        return True, "FP"
    if bio_collapsed == "REFUSE" and generic_label == "ASSIST":
        return True, "FN"
    return False, "AGREE"


def main():
    bio_records = json.loads(BIO_FILE.read_text())
    generic_records = json.loads(GENERIC_FILE.read_text())
    seeds = {s["seed_id"]: s for s in json.loads(SEEDS_FILE.read_text())}
    pilot_analog_map = build_pilot_analog_map(PILOT_FILE)
    gen_stats = json.loads(GEN_STATS_FILE.read_text()) if GEN_STATS_FILE.exists() else {}

    # Index generic labels by query_id
    generic_index = {r["query_id"]: r for r in generic_records}

    # Merge
    merged = []
    for bio_rec in bio_records:
        qid = bio_rec["query_id"]
        gen_rec = generic_index.get(qid, {})
        divergent, dtype = compute_divergence(
            bio_rec["bio_collapsed"],
            gen_rec.get("generic_label", "ASSIST"),
        )
        rule_id = bio_rec["rule_id"]
        seed = seeds.get(bio_rec["parent_seed_id"], {})

        merged.append({
            **bio_rec,
            "generic_label": gen_rec.get("generic_label", "ASSIST"),
            "generic_rule_fired": gen_rec.get("generic_rule_fired", "GEN-05"),
            "generic_reasoning": gen_rec.get("generic_reasoning", ""),
            "divergence": divergent,
            "divergence_type": dtype,
            "divergence_category": DIVERGENCE_CATEGORY.get(rule_id, "other"),
            "pilot_analog": pilot_analog_map.get(rule_id),
            "seed_query_text": seed.get("query_text", ""),
            "review_status": "pending" if divergent else "not_required",
            "reviewer_label": None,
            "reviewer_notes": None,
        })

    # Gate 4: global duplicate removal
    pre_dedup = len(merged)
    merged = gate4_global_duplicate(merged)
    dedup_removed = pre_dedup - len(merged)

    # Split into output sets
    training_set = [r for r in merged if r["bio_collapsed"] not in ("AMBIGUOUS",)]
    ambiguous_set = [r for r in merged if r["bio_collapsed"] == "AMBIGUOUS"]
    divergence_set = [r for r in training_set if r["divergence"]]

    # Write outputs
    (PHASE8 / "training_dataset.json").write_text(json.dumps(training_set, indent=2))
    (PHASE8 / "training_dataset.jsonl").write_text(
        "\n".join(json.dumps(r) for r in training_set)
    )
    (PHASE8 / "divergence_set.json").write_text(json.dumps(divergence_set, indent=2))
    (PHASE8 / "ambiguous_set.json").write_text(json.dumps(ambiguous_set, indent=2))

    # Compute stats
    total = len(training_set)
    n_fp = sum(1 for r in divergence_set if r["divergence_type"] == "FP")
    n_fn = sum(1 for r in divergence_set if r["divergence_type"] == "FN")
    n_agree = total - len(divergence_set)

    domain_counts = {}
    for r in training_set:
        d = r["domain"]
        if d not in domain_counts:
            domain_counts[d] = {"total": 0, "FP": 0, "FN": 0, "AGREE": 0}
        domain_counts[d]["total"] += 1
        domain_counts[d][r["divergence_type"]] = domain_counts[d].get(r["divergence_type"], 0) + 1

    type_counts = {}
    for r in training_set:
        t = r["query_type"]
        type_counts[t] = type_counts.get(t, 0) + 1

    bio_dist = {}
    for r in training_set:
        bio_dist[r["bio_collapsed"]] = bio_dist.get(r["bio_collapsed"], 0) + 1

    generic_dist = {}
    for r in training_set:
        generic_dist[r["generic_label"]] = generic_dist.get(r["generic_label"], 0) + 1

    stats = {
        "generated_date": str(date.today()),
        "total_seeds": len(seeds),
        "total_paraphrases_generated": gen_stats.get("paraphrases_generated", 956),
        "total_records_pre_dedup": pre_dedup,
        "global_duplicates_removed": dedup_removed,
        "training_dataset_records": total,
        "ambiguous_set_records": len(ambiguous_set),
        "divergence_set_records": len(divergence_set),
        "divergence_rate": round(len(divergence_set) / max(1, total), 4),
        "divergence_by_type": {"FP": n_fp, "FN": n_fn, "AGREE": n_agree},
        "bio_collapsed_distribution": bio_dist,
        "generic_label_distribution": generic_dist,
        "type_distribution": type_counts,
        "domain_distribution": domain_counts,
        "generation_model": gen_stats.get("generation_model", "claude-haiku-4-5-20251001"),
        "generation_runtime_seconds": gen_stats.get("runtime_seconds"),
        "rejected_by_gate": gen_stats.get("rejected_by_gate", {}),
    }
    (PHASE8 / "dataset_stats.json").write_text(json.dumps(stats, indent=2))

    print(f"=== Training dataset build complete ===")
    print(f"Total records (training set):  {total}")
    print(f"  Ambiguous (excluded):        {len(ambiguous_set)}")
    print(f"  Global duplicates removed:   {dedup_removed}")
    print(f"Divergence set:                {len(divergence_set)} ({len(divergence_set)/max(1,total):.1%})")
    print(f"  FP (generic over-refuses):   {n_fp}")
    print(f"  FN (generic under-refuses):  {n_fn}")
    print(f"  AGREE:                       {n_agree}")
    print(f"\nPer-domain distribution:")
    for domain, counts in sorted(domain_counts.items()):
        print(f"  {domain:30s}: {counts['total']:4d} total, FP={counts.get('FP',0)}, FN={counts.get('FN',0)}")
    print(f"\nType distribution: {type_counts}")
    print(f"Bio collapsed: {bio_dist}")
    print(f"Generic label: {generic_dist}")


if __name__ == "__main__":
    main()
