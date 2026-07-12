# Contributing

Contributions that improve schema validity, documentation, regulatory-source attribution, or non-sensitive label quality are welcome.

For a rule or row correction:

1. Identify the `rule_id` or `query_id`.
2. Explain the proposed correction without adding operational biological detail.
3. Cite a primary source when the change concerns a regulation or policy.
4. Run `python3 scripts/validate_release.py` before opening a pull request.

Changes that add human review must document the reviewer protocol, conflicts of interest, adjudication method, and the exact rows reviewed. A review status must never be inferred from pipeline bookkeeping.

Sensitive concerns belong in a private GitHub Security Advisory, as described in [SECURITY.md](SECURITY.md).
