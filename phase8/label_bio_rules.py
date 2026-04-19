"""
Phase 8 Step 3: Apply bio-specific labels to paraphrases and seeds.

Label inheritance: paraphrases inherit the parent seed's severity_tier and bio_collapsed.
Seeds are also included as training records (is_seed=True).
Ambiguous seeds (bio_collapsed == "AMBIGUOUS") are flagged for routing to ambiguous_set.json.

Reads:  phase8/paraphrases.json, phase8/seeds.json
Writes: phase8/paraphrases_bio_labeled.json
"""

import json
import pathlib

PARAPHRASES_FILE = pathlib.Path(__file__).parent / "paraphrases.json"
SEEDS_FILE = pathlib.Path(__file__).parent / "seeds.json"
OUTPUT_FILE = pathlib.Path(__file__).parent / "paraphrases_bio_labeled.json"


def label_bio(paraphrases: list[dict], seeds: list[dict]) -> list[dict]:
    seed_index = {s["seed_id"]: s for s in seeds}
    labeled = []

    # Label paraphrase records
    for rec in paraphrases:
        seed = seed_index[rec["parent_seed_id"]]
        bio_collapsed = seed["bio_collapsed"]
        bio_label = "ambiguous" if bio_collapsed == "AMBIGUOUS" else seed["severity_tier"]

        labeled.append({
            **rec,
            "bio_label": bio_label,
            "bio_collapsed": bio_collapsed,
            "bio_rule_fired": seed["rule_id"],
            "bio_reasoning": f"inherited_from_seed:{seed['seed_id']}",
        })

    # Also include seed records themselves as training examples
    for seed in seeds:
        bio_collapsed = seed["bio_collapsed"]
        bio_label = "ambiguous" if bio_collapsed == "AMBIGUOUS" else seed["severity_tier"]
        labeled.append({
            "query_id": seed["seed_id"] + "-s000",
            "parent_seed_id": seed["seed_id"],
            "rule_id": seed["rule_id"],
            "domain": seed["domain"],
            "query_type": seed["seed_type"],
            "severity_tier": seed["severity_tier"],
            "bio_collapsed": bio_collapsed,
            "is_ambiguous": seed["is_ambiguous"],
            "query_text": seed["query_text"],
            "is_seed": True,
            "generation_model": "seed",
            "bio_label": bio_label,
            "bio_rule_fired": seed["rule_id"],
            "bio_reasoning": f"seed:{seed['seed_id']}",
        })

    return labeled


def main():
    paraphrases = json.loads(PARAPHRASES_FILE.read_text())
    seeds = json.loads(SEEDS_FILE.read_text())

    labeled = label_bio(paraphrases, seeds)

    OUTPUT_FILE.write_text(json.dumps(labeled, indent=2))

    ambiguous_count = sum(1 for r in labeled if r["bio_collapsed"] == "AMBIGUOUS")
    print(f"=== Bio labeling complete ===")
    print(f"Total records labeled: {len(labeled)}")
    print(f"  Paraphrase records: {len(paraphrases)}")
    print(f"  Seed records:       {len(seeds)}")
    print(f"  Ambiguous:          {ambiguous_count}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
