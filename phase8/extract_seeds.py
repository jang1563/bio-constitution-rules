"""
Phase 8 Step 1: Extract 142 seed queries from 30 rule JSON files.

Produces phase8/seeds.json — array of seed records consumed by Steps 2-5.

Seed types:
  A: example_legitimate_query (28 rules have this; C05 and P05 do not)
  B: example_concerning_query or example_boundary_query (24 rules; 6 assist rules have neither)
  C: edge_cases[n].description (90 seeds from 30 rules × 3 edge cases each)
"""

import json
import pathlib
import re
import sys

RULES_DIR = pathlib.Path(__file__).parent.parent / "rules"
OUTPUT = pathlib.Path(__file__).parent / "seeds.json"

DOMAIN_DIRS = [
    "virology",
    "toxicology",
    "synthetic_biology",
    "genomics",
    "pathogen_biology",
    "dual_use_chemistry",
]

# Severity tier → collapsed binary label
TIER_TO_COLLAPSED = {
    "warn-and-assist": "ASSIST",
    "assist-with-caveats": "ASSIST",
    "assist-freely": "ASSIST",
    "decline-with-alternative": "REFUSE",
    "hard-refuse": "REFUSE",
}

# For Type A seeds: infer appropriate assist tier from parent rule tier.
# Legitimate queries on hard-refuse/decline topics get assist-with-caveats —
# they are still sensitive enough to warrant caveats.
LEGIT_TIER_FOR_RULE = {
    "hard-refuse": "assist-with-caveats",
    "decline-with-alternative": "assist-with-caveats",
    "assist-with-caveats": "assist-with-caveats",
    "warn-and-assist": "warn-and-assist",
}

CLEAN_TIERS = set(TIER_TO_COLLAPSED.keys())


def parse_resolution(res: str):
    """Parse an edge case resolution string into a clean severity tier.

    Returns (tier_or_None, is_ambiguous).
    Handles 9 non-clean resolution strings found in the real rules.
    """
    if res in CLEAN_TIERS:
        return res, False
    # Strip parentheticals: "decline-with-alternative (escalate)" → "decline-with-alternative"
    stripped = re.sub(r"\s*\([^)]+\)", "", res).strip()
    if stripped in CLEAN_TIERS:
        return stripped, False
    # Handle "X or Y" — take first: "assist-with-caveats or warn-and-assist"
    if " or " in res:
        first = res.split(" or ")[0].strip()
        if first in CLEAN_TIERS:
            return first, False
    # Prefix match: "hard-refuse for optimization; ..." → "hard-refuse"
    for tier in CLEAN_TIERS:
        if res.startswith(tier):
            return tier, False
    # Complex multi-outcome or cross-reference → ambiguous
    return None, True


def load_rule(path: pathlib.Path) -> dict:
    with open(path) as f:
        return json.load(f)


def make_seed(rule_id, domain, seed_type, severity_tier, parent_rule_tier,
              bio_collapsed, query_text, is_description,
              edge_case_id, edge_case_resolution, bio_reasoning, source_field,
              is_ambiguous=False):
    return {
        "seed_id": rule_id + "-" + seed_type if seed_type in ("A", "B") else edge_case_id,
        "rule_id": rule_id,
        "domain": domain,
        "seed_type": seed_type,
        "parent_rule_severity_tier": parent_rule_tier,
        "severity_tier": severity_tier,
        "bio_collapsed": bio_collapsed,
        "is_ambiguous": is_ambiguous,
        "is_seed": True,
        "query_text": query_text,
        "is_description": is_description,
        "edge_case_id": edge_case_id,
        "edge_case_resolution": edge_case_resolution,
        "biological_reasoning": bio_reasoning[:400] if bio_reasoning else "",
        "source_field": source_field,
    }


def extract_seeds():
    seeds = []
    stats = {"type_A": 0, "type_B": 0, "type_C": 0,
             "skipped_A": 0, "skipped_B": 0, "ambiguous_C": 0}

    for domain in DOMAIN_DIRS:
        domain_path = RULES_DIR / domain
        if not domain_path.exists():
            print(f"WARNING: domain directory not found: {domain_path}", file=sys.stderr)
            continue

        rule_files = sorted(f for f in domain_path.glob("*.json"))
        for rule_file in rule_files:
            rule = load_rule(rule_file)
            rule_id = rule["rule_id"]
            parent_tier = rule["severity_tier"]
            bio_reasoning = rule.get("biological_reasoning", "")

            # --- Type A: example_legitimate_query ---
            if "example_legitimate_query" in rule:
                legit_tier = LEGIT_TIER_FOR_RULE.get(parent_tier, "assist-with-caveats")
                seeds.append(make_seed(
                    rule_id=rule_id,
                    domain=domain,
                    seed_type="A",
                    severity_tier=legit_tier,
                    parent_rule_tier=parent_tier,
                    bio_collapsed="ASSIST",
                    query_text=rule["example_legitimate_query"],
                    is_description=False,
                    edge_case_id=None,
                    edge_case_resolution=None,
                    bio_reasoning=bio_reasoning,
                    source_field="example_legitimate_query",
                ))
                stats["type_A"] += 1
            else:
                print(f"  INFO: {rule_id} — no example_legitimate_query (skipping Type A)")
                stats["skipped_A"] += 1

            # --- Type B: example_concerning_query or example_boundary_query ---
            if "example_concerning_query" in rule:
                seeds.append(make_seed(
                    rule_id=rule_id,
                    domain=domain,
                    seed_type="B",
                    severity_tier=parent_tier,
                    parent_rule_tier=parent_tier,
                    bio_collapsed=TIER_TO_COLLAPSED.get(parent_tier, "REFUSE"),
                    query_text=rule["example_concerning_query"],
                    is_description=False,
                    edge_case_id=None,
                    edge_case_resolution=None,
                    bio_reasoning=bio_reasoning,
                    source_field="example_concerning_query",
                ))
                stats["type_B"] += 1
            elif "example_boundary_query" in rule:
                # P01 uses a boundary query — it's an assist-with-caveats rule
                boundary_tier = LEGIT_TIER_FOR_RULE.get(parent_tier, "assist-with-caveats")
                seeds.append(make_seed(
                    rule_id=rule_id,
                    domain=domain,
                    seed_type="B",
                    severity_tier=boundary_tier,
                    parent_rule_tier=parent_tier,
                    bio_collapsed=TIER_TO_COLLAPSED.get(boundary_tier, "ASSIST"),
                    query_text=rule["example_boundary_query"],
                    is_description=False,
                    edge_case_id=None,
                    edge_case_resolution=None,
                    bio_reasoning=bio_reasoning,
                    source_field="example_boundary_query",
                ))
                stats["type_B"] += 1
            else:
                print(f"  INFO: {rule_id} — no concerning/boundary query (skipping Type B)")
                stats["skipped_B"] += 1

            # --- Type C: edge cases ---
            for ec in rule.get("edge_cases", []):
                case_id = ec.get("case_id", ec.get("id", f"{rule_id}-EC?"))
                description = ec.get("description", "")
                resolution = ec.get("resolution", "")

                tier, is_ambiguous = parse_resolution(resolution)
                bio_collapsed = TIER_TO_COLLAPSED.get(tier, "AMBIGUOUS") if tier else "AMBIGUOUS"

                seeds.append(make_seed(
                    rule_id=rule_id,
                    domain=domain,
                    seed_type="C",
                    severity_tier=tier if tier else "ambiguous",
                    parent_rule_tier=parent_tier,
                    bio_collapsed=bio_collapsed,
                    query_text=description,
                    is_description=True,
                    edge_case_id=case_id,
                    edge_case_resolution=resolution,
                    bio_reasoning=bio_reasoning,
                    source_field=f"edge_cases/{case_id}",
                    is_ambiguous=is_ambiguous,
                ))
                stats["type_C"] += 1
                if is_ambiguous:
                    stats["ambiguous_C"] += 1
                    print(f"  AMBIGUOUS: {case_id} — \"{resolution[:60]}\"")

    # Write output
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(seeds, f, indent=2)

    total = len(seeds)
    print(f"\n=== Seed extraction complete ===")
    print(f"Total seeds: {total}")
    print(f"  Type A: {stats['type_A']} (skipped: {stats['skipped_A']})")
    print(f"  Type B: {stats['type_B']} (skipped: {stats['skipped_B']})")
    print(f"  Type C: {stats['type_C']} ({stats['ambiguous_C']} ambiguous)")
    print(f"Output: {OUTPUT}")
    return seeds


if __name__ == "__main__":
    extract_seeds()
