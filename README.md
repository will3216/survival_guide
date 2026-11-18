# The Long After

A satirical but practical post-apocalyptic survival guide.
The book is funny. The advice is real.

- Spec: `docs/superpowers/specs/2026-11-17-long-after-design.md`
- Plan: `docs/superpowers/plans/2026-11-17-long-after.md`
- Manuscript: `manuscript/`
- Reference documents: `notes/`

## Checks

```bash
python3 scripts/lint_manuscript.py          # structural validation
python3 scripts/collect_illos.py            # regenerate the illustration manifest
python3 -m pytest tests/ -q                 # tool tests
```

Illustrations are not generated yet. Every slot carries its own prompt;
`notes/illustration-manifest.json` is the batch input for when they are.
