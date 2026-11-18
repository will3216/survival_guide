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

He has worn glasses since he was nine. The left lens cracked on the first
morning of Y0, during the hour he spent patting a floor for them instead of
filling a bath (chapter 01), and he wore that cracked left lens for nineteen
more years. Nobody is making lenses any more and he knows it. This is
permanent canon from chapter 01 and is available to every later chapter —
chapters 08 (gear), 09 (scavenging), 12 (slow deaths) and 17 especially.
Do not give him good eyesight and do not quietly replace the glasses.

---

## Cast

| Name | What they are | Chapters |
|------|----------------|----------|
| The Spoke | The first group that took him in after the Collapse. Competent, boring, alive. He did not appreciate it at the time. | 01–02 |
| Edda Mull | His neighbour two doors along the landing, eighty-one, on the first morning. Filled her bath before she looked out of the window. Dead before that spring, of age and of nothing being made any more. Chapter 01 only; do not revive her. | 01 |
| The Ninth Hand | A blood cult he ran with for two years. He will tell you it wasn't that bad. It was that bad. | 03, 15 |
| Vera Ott | A mechanic. Taught him the machine chapters. Had no patience for him. Dead by chapter 16. | 08–10, 16 |
| The Bell Country | The settlement he founded and lost. Chapter 15 is his own cautionary material. | 13–16, 18–19 |
| Mother Furnace | A god he invented by committee in an afternoon, for morale. Still worshipped. A six-spoke iron shape. | 11, 18 |
| Ais | The apprentice he is writing this book for. Named rarely. Chapter 20 is addressed to her directly. | 20 |
| T. | The editor of the found manuscript, writing from Ladderwell roughly two generations after the narrator finished the book. Has never seen a working lightbulb and does not entirely believe in them. Signs the editor's preface in `manuscript/00-front-matter.md`. | front matter only |

The Chapters column is a convenience cross-reference, not a mechanical
source of truth — nothing lints it. If a chapter reveals a character
appears in chapters not listed here, update this column by hand in the
same commit as that chapter.

**T. is not Ais.** T. never met the narrator and never met Ais, and knows
Ais only as a name in the manuscript (per the editor's preface and
controller ruling). T. never appears inside a numbered chapter — the
preface is T.'s only appearance — but chapter 20's writer should know T.
exists: T. is the living proof of chapter 20's thesis, a reader with no
referents for the things the book describes.

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

| Name | What it is | First used in chapter |
|------|------------|------------------------|
| The Bell Country | The settlement he founded and lost, nine years in the making and five in the losing. Its first use in the manuscript is chapter 13, the first garden. | 13 |
| Ladderwell | Where T. the editor lives and signs the preface, two generations after the narrator wrote. Editor's era only. | front matter only |

**Ladderwell is off-limits to the narrator.** He never visits it and never
names it — it belongs to T.'s era, two generations after his own, and
chapters 1 through 20 are all his voice. **No chapter from 1 to 20 may
mention Ladderwell.** This is exactly the collision this table exists to
prevent: a chapter writer reaching for a place name should check here
first.

---

## Debts owed by later chapters

Obligations the front matter (`manuscript/00-front-matter.md`) created for
chapters not yet written. Check this section before finishing the chapter
named.

- **Chapter 13 owes four lines about a refrigerator.** The editor's
  preface says the narrator gives four lines, in his chapter on keeping
  food, to "a thing called a refrigerator: a box that was cold inside, all
  the time, by itself, in every house" — and that the editor has read
  those four lines more often than anything else ever written. Chapter 13
  is "Growing Things, Keeping Things." It must contain four lines
  describing a refrigerator that read, to someone two generations later,
  like the kind of thing worth re-reading with longing — not a throwaway
  mention. The preface has already promised the reader this passage
  exists.

---

## Available canon for later chapters

Facts the front matter established that later chapters may draw on
directly. Use them; do not reinvent or contradict them.

- **The Rules are folk-quoted, and quoted wrong.** The editor's preface
  states the Rules are repeated daily, in the yard and over the fire, by
  people who have never read the book and would not read it if handed it
  — and that they get them wrong, and the editor has stopped correcting
  them. This is available canon for **chapter 15** (How Groups Decide
  Things) and **chapter 19** (Holidays, Songs, and Other Load-Bearing
  Nonsense) — the Rules having outgrown the book and become folklore is a
  gift to both a chapter about group governance and a chapter about
  ritual and oral transmission.

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
