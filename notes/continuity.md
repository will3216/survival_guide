# The Long After — Continuity Bible

Reference document. Lives outside `manuscript/`, is never linted. Read this
before naming anything in a chapter — it is the single source of truth for
who is alive, who is dead, what year it is, and which Rule number means what.

Every name recorded here is a name that will appear in `manuscript/`, so
nothing here may collide with `notes/forbidden-terms.txt`. Checked on write.

---

## Narrator

Unnamed throughout the book. People call him by role (the apprentice, the
hand, the old man) or by whatever the current group calls him — never by a
fixed name, and the manuscript never supplies one. Roughly sixty when he
writes this. He was an adult, barely, when the Collapse happened. He has
belonged to eleven groups over the years; six are named in the book.

---

## Cast

| Name | What they are | Chapters |
|------|----------------|----------|
| The Spoke | The first group that took him in after the Collapse. Competent, boring, alive. He did not appreciate it at the time. | 01–02 |
| The Ninth Hand | A blood cult he ran with for two years. He will tell you it wasn't that bad. It was that bad. | 03, 15 |
| Vera Ott | A mechanic. Taught him the machine chapters. Had no patience for him. Dead by chapter 16. | 08–10, 16 |
| The Bell Country | The settlement he founded and lost. Chapter 15 is his own cautionary material. | 14–16 |
| Mother Furnace | A god he invented by committee in an afternoon, for morale. Still worshipped. A six-spoke iron shape. | 11, 18 |
| Ais | The apprentice he is writing this book for. Named rarely. Chapter 20 is addressed to her directly. | 20 |

---

## Timeline

| Year | Event |
|------|-------|
| Y0 | The Collapse. |
| Y0–1 | Alone. |
| Y1 | Taken in by the Spoke. |
| Y3–5 | Runs with the Ninth Hand. |
| Y6 | Meets Vera Ott. |
| Y9–14 | Founds and leads the Bell Country. |
| Y11 | Mother Furnace is invented, for morale. |
| Y14 | The Bell Country ends. |
| Y15+ | Itinerant. Teaches. |
| Y40 | Writes this book. |
| Y40+2 generations | The manuscript is found. |

---

## Places

Invent as needed. Record every place here on first use, so no settlement
gets two names across chapters. This section starts empty by design — later
chapters extend it as they introduce places. Do not pre-populate it with
places no chapter has used yet.

*(No places recorded yet. The next chapter to introduce a settlement, ruin,
or landmark adds a row below.)*

| Name | What it is | First used in chapter |
|------|------------|------------------------|

---

## Rule ledger

A Markdown table with columns `| # | Rule | Chapter |`. **Every row must
begin with the number so `scripts/lint_manuscript.py`'s `LEDGER_ROW_RE` can
read it** — do not reformat this table, do not indent it, do not reorder the
columns.

Add a row here in the **same commit** as the chapter that first cites the
Rule. `check_rules_cited` fails the build on any `Rule N` mentioned in a
chapter whose number is not a row below.

| # | Rule | Chapter |
|---|------|---------|
| 4 | Count before you move. | 01 |
| 9 | Water first. Always. | 04 |
| 11 | The second floor is not safer. It is only harder to leave. | 02 |
| 80 | *Reserved. Spent in chapter 20. Do not cite before then.* | 20 |

**Rule 80 is reserved.** It is the final rule — the soft rule that outranks
the hard ones. Its number and chapter are seeded here now so the ledger is
complete, but its text is deliberately not written in this task. It is
written only in chapter 20. **No chapter before chapter 20 may cite Rule
80.** The linter cannot enforce this — `check_rules_cited` would happily
pass an early citation — so this is an editorial rule, not a mechanical one.
Treat it as load-bearing anyway.
