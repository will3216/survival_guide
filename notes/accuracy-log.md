# The Long After — Accuracy Log

Reference document. Lives outside `manuscript/`, is never linted for prose,
but its headings are machine-read by `scripts/lint_manuscript.py`
(`read_accuracy_chapters`), which requires one `## Chapter NN` heading (two
digits, zero-padded) for every chapter listed in `notes/manuscript-order.txt`.
Missing a heading produces an `ACCURACY` error.

This file is the real-world basis for every load-bearing claim in the book —
the technique behind the joke — kept separate from the manuscript so the
voice can stay funny while the underlying advice stays auditable. Section 1
of `notes/style-guide.md` is the reason this file exists: a reader who
follows the book's instructions in an actual emergency must be better off,
not worse. Every instruction with real-world stakes gets an entry here when
its chapter is written.

## Entry format

```markdown
- **Claim as stated in the chapter.** Basis: [source and what it says]. Confidence: high | conservative-choice | vague-on-purpose.
```

- **Claim as stated in the chapter** — quote or closely paraphrase the line
  from the manuscript so the claim and its justification can be checked side
  by side.
- **Basis** — the real-world source: a field, a standard practice, a named
  reference work, or basic physics/chemistry/physiology. Specific enough that
  someone could go check it.
- **Confidence** — one of:
  - `high` — well-established, verifiable technique.
  - `conservative-choice` — multiple valid approaches exist; the book picked
    the safer one on purpose.
  - `vague-on-purpose` — the chapter is deliberately imprecise (e.g. no exact
    dosage) because precision would be irresponsible without context the
    reader can't supply.

Each chapter's section starts as `_No entries yet._`. That string means
exactly one thing: **nobody has written this chapter, or nobody has logged
it yet.** It is a placeholder, not a verdict, and it must not be left in
place once a chapter is written and reviewed for claims.

When a chapter is written, its section gets one of two outcomes, and
leaving it ambiguous between them is the bug this format exists to prevent:

- **Claims exist.** Replace `_No entries yet._` with the bulleted list of
  entries, one per claim, in the format above.
- **No load-bearing claims exist.** Replace `_No entries yet._` with
  `_Reviewed — nothing load-bearing to log._` This string means a human
  checked this chapter for real-world claims and found none worth an
  entry. It is not the default and must never be left in place without
  that check having happened.

`_No entries yet._` must never be the final state of a written chapter's
section. If a chapter is done and its section still reads `_No entries
yet._`, that is a sign the accuracy review was skipped, not that the
chapter made no claims.

---

## Chapter 01

_No entries yet._

## Chapter 02

_No entries yet._

## Chapter 03

_No entries yet._

## Chapter 04

_No entries yet._

## Chapter 05

_No entries yet._

## Chapter 06

_No entries yet._

## Chapter 07

_No entries yet._

## Chapter 08

_No entries yet._

## Chapter 09

_No entries yet._

## Chapter 10

_No entries yet._

## Chapter 11

_No entries yet._

## Chapter 12

_No entries yet._

## Chapter 13

_No entries yet._

## Chapter 14

_No entries yet._

## Chapter 15

_No entries yet._

## Chapter 16

_No entries yet._

## Chapter 17

_No entries yet._

## Chapter 18

_No entries yet._

## Chapter 19

_No entries yet._

## Chapter 20

_No entries yet._
