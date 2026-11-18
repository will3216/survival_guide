# The Long After — Design Spec

**Date:** 2026-11-17
**Status:** Approved for implementation planning
**Deliverable:** A satirical but practical full-length post-apocalyptic survival guide, in Markdown, illustrated.

---

## 1. Premise

A survival manual written by a man who lived through the Collapse and ran with
roughly a dozen post-apocalyptic groups — some good, most not. He has led,
followed, floundered, and flourished, and he is writing it all down for the
apprentice who will outlive him.

The book is funny. The advice is real. Those two facts are held in tension by a
single rule, stated here because every other decision in this spec descends
from it:

> **The narrator is never ironic about technique.**

Comedy comes from his framing, his anecdotes, and his unhinged sense of what is
normal. It never comes from giving the reader bad information. A reader who
follows this book's instructions in an actual emergency should be better off,
not worse.

**Working title:** *The Long After: A Practical Guide for Whoever Finds This*

**Target length:** 20 chapters, ~2,000–3,000 words each, 45,000–55,000 words
total, plus front matter and appendices.

### Framing device

A found manuscript. One voice, written by hand, water-stained, discovered two
generations later. The book opens with a short fictional editor's preface by
someone who has never seen a working lightbulb, explaining where the pages were
found and which ones are missing.

### Tone register

Mostly light with a dark undertow. The book is primarily funny and warm. The
horror of what happened arrives in single-line asides — dropped, not dwelt on,
at most one per chapter. A trapdoor, not a theme.

The book's argument, never stated outright but structurally unavoidable: what
kept people alive was cooperation, ritual, and absurd joy.

---

## 2. Structure

Organized by distance from the event, which is how real emergency guidance is
ordered. The structure is itself a straight-faced joke that happens to be
correct, and it earns the ending: Part I is about not bleeding to death, and
Part V is about inventing a god — because by then, culture *is* the survival
skill.

### Front matter — `manuscript/00-front-matter.md`

1. **Author's note (real voice).** Four plain lines: this is a comedy, the
   techniques are accurate to the best of our knowledge as of writing, and
   nobody should learn medicine from a novel. Not in character. Non-negotiable.
2. **Editor's preface (in fiction).** The lightbulb-naive editor, the found
   pages, the missing chapters.
3. **Contents.**

### Part I — The First Hour
*What kills you before you have a plan.*

| # | Chapter | Practical core |
|---|---------|----------------|
| 1 | Triage: Decide What You Are | The rule of threes; panic as a cause of death; ordering your own problems |
| 2 | Run or Dig In | Shelter-in-place vs. evacuation; the bag you should already own |
| 3 | The Body Is Your First Vehicle | Bleeding control, shock, fractures, and what you cannot fix |

### Part II — The First Week

| # | Chapter | Practical core |
|---|---------|----------------|
| 4 | Water, and the Lies People Tell About It | Sourcing, filtration, boiling, chemical treatment |
| 5 | Two Ways Weather Kills You | Hypothermia and hyperthermia; insulation; fire |
| 6 | Food Matters Later Than You Think | Calorie math; stores; why foraging is mostly a hobby |
| 7 | The First People You Meet | Threat assessment, approach, trade, walking away |

### Part III — The First Year

| # | Chapter | Practical core |
|---|---------|----------------|
| 8 | Gear That Earns Its Weight | Kit philosophy, redundancy, maintenance |
| 9 | Scavenging Is a Profession | Systematic search of structures and vehicles |
| 10 | The Machine | Fuel sourcing and storage, engine triage, tires, honest limits |
| 11 | Voices Across the Waste | Radio, signaling, dead drops, maps, navigation |
| 12 | Rot, Teeth, and Other Slow Deaths | Sanitation, latrines, dental, wound care |

### Part IV — The Long After

| # | Chapter | Practical core |
|---|---------|----------------|
| 13 | Growing Things, Keeping Things | Catchment, soil, seed saving, drying/salting/fermenting |
| 14 | The Economy of Nothing | Barter, debt, pricing, spotting bad faith |
| 15 | How Groups Decide Things | Councils, rationing, exile, the failure modes of cults |
| 16 | Grief, Boredom, and Morale | The two killers nobody preps for |

### Part V — What Comes After You

| # | Chapter | Practical core |
|---|---------|----------------|
| 17 | The Silhouette of Belonging | Dress as in-group signal; a tribe you can read at 300 yards |
| 18 | On the Manufacture of Gods | Designing a deity, writing its origin story, what makes one stick |
| 19 | Holidays, Songs, and Other Load-Bearing Nonsense | Ritual calendars, feasts, naming, oaths |
| 20 | Teaching the Ones Who Never Saw a Lightbulb | Apprenticeship, transmission, writing it down anyway |

Part V is absurd on its surface and sincere underneath. Costume is in-group
signaling, ritual is cohesion technology, and shared myth is cheaper than
enforcement — all of which is true, and all of which the narrator teaches
with a completely straight face.

### Back matter — `manuscript/99-appendices.md`

Quick-reference tables pulled out of the chapters: water treatment ratios,
bleeding control sequence, barter value guide, and a blank god-design
worksheet.

---

## 3. Voice and apparatus

### Voice rules

- First person, past-weathered. Short declaratives.
- He is never winking. No jokes told; a worldview reported.
- He addresses the reader directly and assumes they are an idiot he has decided
  to help anyway.
- Dark material: one aside per chapter maximum, unremarked and not revisited.
- No *Mad Max* proper nouns. The aesthetic is borrowed; every faction, god,
  place, and person is original.

### Per-chapter apparatus

Identical furniture in every chapter, so it reads as a real manual:

1. **Epigraph** — a line of in-world text: graffiti, a catechism, a verse of a
   work song.
2. **Opening** (~300 words) — one specific memory, one named person, setting up
   the chapter's problem.
3. **The instruction** (~1,500–2,000 words) — accurate prose, numbered
   procedures, tables where tables belong.
4. **"What It Costs You"** — boxed sidebar on tradeoffs and failure modes.
   Where he is blunt about what the technique takes from you.
5. **"The Short Version"** — closing checklist, 5–9 lines, actionable without
   having read the chapter.

### Recurring cast

Continuity across 20 chapters so the book reads as one life rather than
twenty essays.

| Name | Role |
|------|------|
| **The Spoke** | The first group that took him in. Competent, boring, alive. He did not appreciate it. |
| **The Ninth Hand** | The blood cult he ran with for two years. He will tell you it wasn't that bad. It was that bad. |
| **Vera Ott** | The mechanic who taught him the machine chapters and had no patience for him. |
| **The Bell Country** | The settlement he founded and lost. Chapter 15's cautionary material is his own. |
| **Mother Furnace** | A god he invented by committee in an afternoon, for morale. She outlived her makers and is still worshipped. Chapter 18 is told through her. |
| **Ais** | The apprentice he is actually writing this for. Named rarely. Chapter 20 is addressed to her. |

Mother Furnace is the book's central engine: a deity the narrator knows is
fabricated, built deliberately for morale, that demonstrably worked. She is the
straight-faced-narrator contract at full strength.

---

## 4. Accuracy discipline

The premise collapses if the advice is wrong, so:

- **No invented numbers.** Treatment ratios, tourniquet placement, water and
  calorie minimums, canning and fermentation safety, fuel storage life — these
  come from established real-world guidance or they do not appear.
- Where real guidance is genuinely contested, the narrator takes the
  conservative position and says why.
- Anything uncertain is written vaguer rather than wronger.
- `notes/accuracy-log.md` records the real-world basis for every load-bearing
  claim, so the book's honesty can be audited separately from its voice.

### Content boundaries

Independent of narrator or framing, two things stay off the page:

1. Weapons and explosives manufacture.
2. Operationalized coercive-control technique.

Chapters 15 and 18 handle cults from the inside, as **failure modes to
recognize**. The narrator is candid that the Ninth Hand's methods worked on him,
which is both the honest treatment and the funnier one. Mother Furnace is built
in the open, by committee, for morale — and he states plainly where that line
sits and what crossing it looked like.

---

## 5. Illustrations

Comical, cartoonish illustrations generated later via nano banana. Generation is
deliberately punted; the **style guide, slot placement, and manifest pipeline
are built now**, because illustration consistency is determined by the style
guide and not by the generator.

### Style DNA

Two-ink civil-defense manual: flat black line plus one rust-orange spot color,
paper-grain ground, no gradients and no rendered lighting, rubbery cartoon
figures with simple bean-shaped bodies and heavy outlines.

Chosen for two reasons. It is the correct joke — the book *is* a straight-faced
government pamphlet. And it is the most forgiving style for consistency across
~60 images, because a flat two-ink look has almost nothing in it to drift.

### Two classes, different rules

- **Plates** — actually teach. Numbered callouts, labeled parts, correct
  technique. Reviewed against the accuracy log exactly as prose is. An
  inaccurate plate is worse than no plate.
- **Marginalia** — gags. Mother Furnace's official portrait, a comparison chart
  of tribe silhouettes, Vera Ott's expression. Never load-bearing.

Budget: ~3 per chapter, roughly 1 plate and 2 marginalia. ~60 total.

### Consistency plan

`notes/illustration-style.md` holds:

- The **fixed prompt preamble** — the exact style sentence prepended to every
  generation, verbatim, every time.
- The palette, in hex.
- The do-not list: no gradients, no photoreal faces, no text in the image
  beyond callout numbers.
- **Character and object sheets.** The first generation run produces one
  reference sheet per recurring character and per repeated object; every
  subsequent generation passes those in as reference images. Characters stay
  silhouette-identifiable — Vera is overalls plus a pushed-up welding mask,
  Mother Furnace is always the same six-spoke iron shape.

### Placeholders

Every illustration slot is written into the manuscript during drafting, as a
block that carries its own generation prompt:

```markdown
<!-- ILLO
id: 04-plate-01
class: plate
caption: Figure 4.1 — The three-stage filter, and the stage everyone skips.
alt: Cutaway of a layered gravel, sand, and charcoal filter in a cut barrel.
prompt: Cutaway diagram of a three-layer water filter in a cut oil drum...
-->
![Figure 4.1 — The three-stage filter, and the stage everyone skips.](../illustrations/04-plate-01.png)
```

The comment block is the source of truth; the image link resolves the moment the
file lands at that path. `scripts/collect_illos.py` extracts every block into
`notes/illustration-manifest.json`, so wiring up nano banana later is one batch
pass over the manifest rather than a hunt through twenty files.

**The prose is written to stand alone.** Every chapter must read completely
without a single image present.

---

## 6. Repository layout

```
survival_guide/
  README.md
  docs/superpowers/specs/2026-11-17-long-after-design.md
  manuscript/
    00-front-matter.md        author's note, editor's preface, contents
    01-triage.md … 20-teaching.md
    99-appendices.md          reference tables, god-design worksheet
  notes/
    style-guide.md            voice rules, apparatus template
    continuity.md             cast, factions, gods, timeline
    accuracy-log.md           real-world basis per load-bearing claim
    illustration-style.md     prompt preamble, palette, character sheets
    illustration-manifest.json  generated
  illustrations/              empty until generation
  scripts/
    collect_illos.py
```

---

## 7. Workflow

1. Write `notes/style-guide.md`, `notes/continuity.md`, and
   `notes/illustration-style.md` **before** chapter 1. The voice and the cast
   are decided once, in writing, and then obeyed.
2. Draft chapters in order. One git commit per chapter.
3. **Review checkpoint at the end of each Part.** Drafting stops, the user reads
   3–5 chapters, and voice or density is corrected before more is written.

Checkpoint 3 matters at this length: discovering in chapter 18 that the
narrator's register is wrong would waste 40,000 words.

### Definition of done

- 20 chapters plus front and back matter, 45k–55k words.
- Every chapter carries all five apparatus elements.
- Every load-bearing factual claim has an entry in the accuracy log.
- Every chapter has its illustration slots placed, with prompts written.
- `notes/illustration-manifest.json` generates cleanly from the manuscript.
- The book reads correctly with zero images present.

Illustration generation itself is explicitly **out of scope** for this spec and
becomes its own task once nano banana is connected.
