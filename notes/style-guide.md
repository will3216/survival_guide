# The Long After — Style Guide

Reference document. Lives outside `manuscript/`, is never linted, is never
published. The forbidden-terms list applies only to files under `manuscript/`,
which is why this document can name its touchstones out loud.

Read this in full before writing any chapter. It is short on purpose.

---

## 1. The one rule

> **The narrator is never ironic about technique.**

Comedy comes from his framing, his anecdotes, and his sense of what is normal.
It never comes from giving the reader bad information.

A reader who follows this book's instructions in an actual emergency must be
better off, not worse. Every other rule in this document is downstream of that
one. When any rule here appears to conflict with this one, this one wins.

Practically, this means: you may joke about *who* taught him a technique, *what
it cost him* to learn it, or *what he thinks is reasonable*. You may never joke
inside the procedure itself. A number is never a punchline. A step order is
never a punchline. If a technique is genuinely uncertain, he says so flatly —
that is not a joke either.

---

## 2. Voice

**First person, past-weathered.** He is writing by hand, late, for an
apprentice who will outlive him. He has already done this; he is reporting, not
speculating.

**Short declaratives.** Sentence length is mostly short, occasionally long when
a list of consequences earns it. No ornament. No rhetorical questions stacked
for effect.

**He never winks.** No jokes are *told*. A worldview is *reported*. The humor is
the gap between how extraordinary a thing is and how ordinary he finds it. If a
sentence could be read aloud as a bit, cut it back until it reads as testimony.

**He addresses the reader directly**, and assumes they are an idiot he has
decided to help anyway. Affectionate contempt, trending toward affection. He is
blunt because he does not want them to die, not because he is above them. "You"
is normal. "Do this." "Do not do this." "You will not do this, and then you will,
and then you will remember I said it."

**Specificity over flourish.** A named person and a real number beat an
adjective, every time. Not "it was bitterly cold" but "Marta read minus eleven
on the porch thermometer and said that was the warm part of the night." Invent
names freely; keep them plain and keep them consistent (see
`notes/continuity.md`). Give quantities: hours, litres, degrees, grams, paces,
how many people, how many were left.

**Sincerity is allowed and is not apologized for.** When he means something, he
says it in one plain sentence and moves on. He does not undercut it afterward.

---

## 3. Tone touchstones

Two references, with a strict division of labor. The split is the mechanism that
keeps the dark undertow from curdling:

> *"the narrator has seen Mad Max things and tells them in a Zombieland voice."*

| Touchstone | Governs | Specifically |
|------------|---------|--------------|
| **Zombieland** | Voice, violence, instructiveness | Warm, deadpan, personally earned advice. Numbered rules. Violence reads cartoonish rather than harrowing. Sincerity arrives suddenly and is not apologized for. |
| **Mad Max** | World only | Scarcity economy, faction iconography, vehicular culture, grotesque pageantry, the aesthetics of rust and chrome. |

**Neither contributes proper nouns.** No characters, places, vehicles, or
factions from either. Numbered survival rules are a genre convention, not
borrowed IP. The manuscript linter enforces this against
`notes/forbidden-terms.txt`; the right move is not to work around the list but
never to need it.

The failure mode to watch for is **crossing the streams**: Mad Max violence
described in Mad Max register (harrowing, operatic, dwelt upon) instead of in
the Zombieland register (brisk, absurd, already survived). The world is grim.
The telling is not.

---

## 4. The dark aside

**One per chapter. Maximum. Often zero.**

One or two sentences. Dropped without comment and never revisited — no
follow-up paragraph, no callback later in the chapter, no return in a later
chapter. A trapdoor, not a theme. The next sentence after a dark aside goes
straight back to the technique, as though nothing happened, because to him
nothing did.

> Good: "We buried four that winter. The ground was easier than I expected,
> which is its own kind of bad news."

> Bad: anything that spends a paragraph on it, or that asks the reader to feel
> something specific.

Tests for an aside before you keep it:

- Is it two sentences or fewer?
- Does the paragraph after it ignore it completely?
- Does it report a fact rather than instruct the reader how to feel about it?
- Is it the only one in the chapter?

Any "no" means cut it or shrink it. Banned in all cases: the second dark aside
(see section 7).

---

## 5. The Rules

The Rules are the book's recurring device: terse, deadpan, personally earned,
and **actually correct**. A Rule is compressed real advice. The comedy is in the
compression, never in the content being wrong.

- **Terse.** One line. Ideally under twelve words.
- **Deadpan.** Stated flat, as settled fact, with no setup and no explanation
  attached. The chapter explains it; the Rule does not.
- **Personally earned.** It sounds like something that cost him.
- **Correct.** Never invent a Rule that is funny but wrong. If the funny version
  of a Rule would get the reader hurt, you write the correct version and find
  the comedy somewhere else in the chapter. This is section 1 applied.

**Numbering is non-sequential and never reconciled.** Rule 4 can be followed by
Rule 61 and then Rule 9. He does not remember them in order and makes no
apology. There are gaps, and the gaps are never explained in-text. Do not
renumber to tidy up; do not invent a scheme.

**Ledger discipline — this one will break the build.** Every `Rule <number>` a
chapter mentions must exist as a row in the Rule ledger in `notes/continuity.md`.
`lint_manuscript.check_rules_cited` extracts every `Rule N` from a chapter and
fails on any number that is not a ledger row. So:

> A new Rule must be added to the `notes/continuity.md` ledger **in the same
> commit** as the chapter that cites it, or the linter fails.

Before coining a Rule, read the ledger. Reuse an existing Rule rather than
duplicating its advice under a new number, and never reuse a number for
different advice.

---

## 6. The chapter skeleton

Copy this literally. The headings `## What It Costs You` and
`## The Short Version` are matched character-for-character by the linter —
not the wording, not a variation, exactly these. The blockquote epigraph must
appear within the first twelve lines of the file. `The Short Version` must be
followed by between 5 and 9 lines beginning `- `.

```markdown
# Chapter N: Title

> Rule NN: The rule, stated flat.

[Opening: ~300 words. One memory, one named person, the chapter's problem
made concrete. Ends by turning to the reader.]

## [Instruction heading]

[The real content. Numbered procedures where order matters. Tables where
tables belong. ~1,500-2,000 words total across however many headings.]

## What It Costs You

[Tradeoffs and failure modes. Where he is blunt about the price of the
technique. 150-250 words.]

## The Short Version

- [5-9 bullets, actionable without having read the chapter. May cite Rules
  by number.]
```

Notes on the parts:

- The **epigraph** is a Rule, in a blockquote, on its own. It is the chapter's
  thesis in one flat line.
- The **instruction headings** are yours: use as many `##` headings as the
  material needs, titled in his voice rather than as textbook labels.
- **What It Costs You** is not a disclaimer section. It is where he is honest
  about the price, the failure modes, and what the technique trades away.
- **The Short Version** must stand alone. A reader who has read nothing else
  should be able to act on it. Count the bullets: 5 minimum, 9 maximum.

Chapters also carry `<!-- ILLO ... -->` illustration blocks; their format is
owned by `notes/illustration-style.md` (Task 7), not by this skeleton. One
mechanical warning if you write one: a `prompt:` value must be a single line or
use indented continuation lines. Never a YAML block scalar (`prompt: >`) — the
parser has no block-scalar handling and will not read it.

---

## 7. Banned moves

- **No winking at the reader.** No nudge, no "but I digress," no acknowledgment
  that any of this is funny.
- **No "little did I know,"** and no other foreshadowing of that shape. He is
  not building suspense; he is handing over a manual.
- **No chapter that opens with a dictionary definition.** Or an etymology, or a
  quotation from anyone outside the book.
- **No pre-Collapse brand names.** No product names, no companies, no
  trademarks. Describe the object: "a red two-stroke generator," not a make.
- **No describing the Collapse's cause.** He does not know and does not care,
  and the book is stronger for it. No theories, no hints, no "when the X
  happened." It happened. He was there. That is all.
- **No second dark aside.** One per chapter is the ceiling (section 4).
- **No irony about technique.** Restated here because it is the one that
  matters (section 1).

---

## 8. Word budget

**1,800–3,200 words per chapter**, enforced by `scripts/lint_manuscript.py`
(`WORDS_MIN` / `WORDS_MAX`). The count is taken after HTML comments are
stripped, so `<!-- ILLO ... -->` blocks do not count toward it.

Target the middle — roughly 2,000–3,000 words — so that edits in either
direction do not push a chapter out of bounds. Rough internal split:

| Part | Words |
|------|-------|
| Opening | ~300 |
| Instruction sections | ~1,500–2,000 |
| What It Costs You | 150–250 |
| The Short Version | the rest |

Run `python3 scripts/lint_manuscript.py` before committing a chapter. A chapter
that fails is not finished.
