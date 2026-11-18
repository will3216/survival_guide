# The Long After — Design Spec

**Date:** 2026-11-17 (narrator redesigned 2026-11-18)
**Status:** Approved for implementation
**Deliverable:** A satirical but practical full-length post-apocalyptic survival guide, in Markdown, illustrated.

---

## 1. Premise

A survival manual written by a man who was nobody.

He was a grunt before the Collapse and a grunt after it. He carried things for
a living; the book never says much more than that, because he does not find it
interesting. He was never in charge of anything. He was present for events that
other people tell stories about, generally holding something, usually facing
the wrong way. Everything he knows about staying alive he learned afterwards,
by getting it wrong first, cheerfully, several times.

He does not know there was a story. Not that he was a minor character in one —
that one existed at all. He was living his life. It happened to be the end of
the world.

**The book is funny. The advice is real.** Those two facts are held in tension
by a single rule, stated here because every other decision descends from it:

> **The narrator is never ironic about technique.**

Comedy comes from what he fails to notice, what happens to his body, and his
unshakeable good mood. It never comes from giving the reader bad information.

### The contract

The second structural rule, and the one that makes the first one safe:

> **The prose may miss the point. "The Short Version" never does.**

A chapter may wander, bury its own lesson in an anecdote, and move on without
noticing what it just taught. The checklist at the end of every chapter is
where his competence appears undiluted: clean, correct, ordered, actionable.
He writes both. He is a practical man who makes lists, and he would be puzzled
to hear that the list was the important part.

This is what lets him be oblivious without ever endangering a reader. **Being
oblivious about significance is not the same as being unreliable about
technique.** He is completely trustworthy on how; he simply has no idea that
the week he is describing was the famous one.

Some of what he teaches, he does not know he is teaching. He describes what he
does. The reader extracts the method. He never offers it as instruction.

**Working title:** *The Long After: A Practical Guide for Whoever Finds This*

**Target length:** 20 chapters, ~2,250–2,750 words each, 45,000–55,000 words
total, plus front matter and appendices.

### Framing device

A found manuscript. One voice, handwritten, water-stained, discovered two
generations later. The book opens with a short preface by an editor, **T.**,
who has never seen a working lightbulb and does not entirely believe in them.

T. believes they are editing the work of the great authority on staying alive.
The reader can see that T. is editing a man who kept getting run over. Neither
of them is wrong.

### Tone register

**Comically upbeat, against the content.** He is relentlessly, genuinely
cheerful about an apocalypse. Nothing is a tragedy; everything is a thing that
happened and can be worked around. This is not denial and it is not a coping
mechanism he is visibly operating — it is simply his temperament, and it is the
reason he survived twenty years of things that killed better men.

The darkness does not arrive in a designated aside. **It arrives in things he
says brightly and walks straight past.** The reader flinches. He does not
notice. He is already on to the next practical point.

The book's argument, never stated outright: the people who got the songs are
dead, and the man who carried their water is not.

### Comedy engines

Three, braided, rotating by chapter. **No bitterness in any of them.**

1. **Bodily consequences.** Every technique exists because it happened to him
   first. Motorcycles are fun, and you will be hit by one. He has been set on
   fire slightly, fallen through two roofs, and been run over while chasing
   someone who turned out to be a coat on a fence.
2. **Proximity to glory, facing the wrong way.** He was forty feet from famous
   moments and remembers the weather. His account of a legendary event is
   boring, specific, and quietly contradicts the version everyone knows.
3. **Unglamorous expertise.** He is genuinely excellent at drainage, knots,
   queueing, load-bearing and rot, and he has never once thought of himself as
   an expert at anything.

### Tone touchstones

| Touchstone | Governs | Specifically |
|------------|---------|--------------|
| **Zombieland** | Voice, violence, instructiveness | Deadpan, personally earned advice. Numbered rules. Violence reads cartoonish rather than harrowing. Sincerity arrives suddenly and is not apologized for. |
| **Mad Max** | World only | Scarcity economy, faction iconography, vehicular culture, grotesque pageantry, rust and chrome. |

Neither contributes proper nouns.

---

## 2. Structure

Organized by distance from the event, which is how real emergency guidance is
ordered. Each chapter keeps its practical core; what changed in the redesign is
the angle of every anecdote and what he fails to notice in it.

### Front matter — `manuscript/00-front-matter.md`

1. **Author's note (real voice).** Four plain lines: this is a comedy, the
   techniques are accurate as of writing, it is not a substitute for training,
   nobody should learn medicine from a novel. Not in character.
2. **Editor's preface (in fiction).** T., two generations later.
3. **Contents.**

### Part I — The First Hour
*What kills you before you have a plan.*

| # | Chapter | Practical core |
|---|---------|----------------|
| 1 | Triage: Decide What You Are | The rule of threes; panic as a cause of death; ordering your own problems |
| 2 | Run or Dig In | Shelter-in-place vs. evacuation; the bag you should already own |
| 3 | The Body Is Your First Vehicle | Bleeding, shock, fractures, and what you cannot fix |

### Part II — The First Week

| # | Chapter | Practical core |
|---|---------|----------------|
| 4 | Water, and the Lies People Tell About It | Sourcing, filtration, boiling, chemical treatment |
| 5 | Two Ways Weather Kills You | Hypo/hyperthermia; insulation; fire |
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
| 17 | The Silhouette of Belonging | Dress as in-group signal; a tribe readable at 300 yards |
| 18 | On the Manufacture of Gods | Designing a deity, its origin story, what makes one stick |
| 19 | Holidays, Songs, and Other Load-Bearing Nonsense | Ritual calendars, feasts, naming, oaths |
| 20 | Teaching the Ones Who Never Saw a Lightbulb | Apprenticeship, transmission, writing it down anyway |

Part V is absurd on its surface and sincere underneath — and in the redesign it
is funnier, because he witnessed all of it from the bottom and understood none
of it as it happened. Costume is in-group signaling, ritual is cohesion
technology, shared myth is cheaper than enforcement. All true. He thought they
were assigning chores.

### Back matter — `manuscript/99-appendices.md`

1. **The Rules, As Best I Remember Them.** A partial list with numbered gaps —
   most forgotten, exactly two marked `[page torn]`.
2. Quick-reference tables: water treatment, bleeding control, barter values.
3. A blank god-design worksheet.

---

## 3. Voice and apparatus

### Voice rules

- First person, cheerful, physical, unpretentious. Short declaratives.
- **He is always in a good mood.** Setbacks are interesting rather than tragic.
- He is never winking. He does not know there is anything to wink about.
- He addresses the reader directly, as one working person to another.
- **He under-reports.** The worse the event, the more casually it is mentioned.
- He does not editorialize about significance, because he does not perceive it.
- No *Mad Max* or *Zombieland* proper nouns. Every faction, god, place and
  person is original.

### What he does not notice

A running technique, not an occasional joke. In every chapter he should fail to
register at least one of:

- that the event he is describing is the one people tell stories about
- that the person he is describing became someone
- that the thing he did was difficult, brave, or clever
- that the lesson he just delivered was a lesson

Never signposted. The reader does the work.

### The Rules

The book's spine and running gag. Numbered, cited out of order from an implied
corpus of roughly eighty, terse, deadpan, personally earned and **actually
correct**.

> Rule 9: Water first. Always.
> Rule 11: The second floor is not safer. It is only harder to leave.

Mechanics:

- An epigraph may be a Rule instead of in-world text.
- "The Short Version" may cite Rules by number.
- A Rule is compressed real advice; the comedy is in the compression, never at
  the expense of the advice being true.
- Numbering is non-sequential and never reconciled.
- **He has no idea they became folklore.** He thinks they are things he tells
  himself to avoid repeating a mistake. T.'s preface reveals they are quoted
  daily, in every house, by people who never read the book and get them wrong.
  He is the de facto authority on staying alive and will never learn it.
- **One rule is held in reserve** and spent in chapter 20, addressed to Ais.

`notes/continuity.md` holds the authoritative Rule ledger. A Rule cited in a
chapter must have a row there, added in the same commit, and no chapter may
cite a Rule whose ledger chapter is later than its own.

### The editor's interventions

T. does not stay in the margins. Throughout the book, the editor breaks role to
react to what the narrator has just said — and this is the second voice the
reader hears.

> **— T.** He is describing the night the Bellwright died. He gives it four
> lines and then returns to the subject of drainage. I have read this passage
> more times than I can defend.

Mechanics:

- Rendered as a blockquote opening `> **— T.**`, placed immediately after the
  passage it reacts to. Never inside a numbered procedure.
- **One to three per chapter.** At least one per chapter should be the
  exasperated kind — some version of *no, that is not the takeaway* — where an
  eloquent person briefly stops being eloquent.
- **T. never corrects the technique.** This is inviolable. T. corrects
  *meaning*, never method. Where T. touches a technique at all it is to confirm
  it, or to note having seen it work. A reader must never be left unsure
  whether the instruction is sound.
- T.'s register is formal, affectionate and precise, and the joke is that
  precision failing under pressure. T. is cleverer than the narrator and more
  perceptive about people, while being naive about the vanished world — still
  reverent about the wrong things, still unsure about lightbulbs.
- T. sees what the narrator cannot: that he was present at famous events, that
  the people he mentions in passing were legends, that his Rules became
  folklore, and that the lesson in a chapter is frequently not the one he
  thought he was giving.
- **T. never appears after `## The Short Version`.** That checklist is the
  narrator's, it is the last text in the file, and nothing follows it.

The two voices never meet. T. is answering a man who has been dead for two
generations, and the narrator will never know he was read.

### Per-chapter apparatus

1. **Epigraph** — a Rule, or in-world text.
2. **Opening** (~300 words) — one specific memory, one named person, a problem
   made concrete. Usually something going wrong with his body.
3. **The instruction** (~1,500–1,800 words) — accurate prose, numbered
   procedures, tables where tables belong.
4. **"What It Costs You"** — a boxed sidebar on tradeoffs and failure modes.
   Blunt about price. Not a second emotional outlet.
5. **"The Short Version"** — 5–9 terse bullets, actionable without the chapter.
   **The last text in the file**, because the linter counts every `- ` line
   from that heading to end of file.

### Recurring cast

He is present for all of it and responsible for none of it.

| Name | Role |
|------|------|
| **The Spoke** | The first group that took him in. Competent, boring, alive. He fetched and carried. |
| **The Ninth Hand** | A blood cult he did chores for, two years. He thought the robes were a uniform issue. He will tell you it wasn't that bad. It was that bad. |
| **Vera Ott** | Mechanic. His teacher, and he was her hands. Dies in chapter 16. |
| **The Bellwright** | Founded the Bell Country. A legend to everyone else. To him, a man with strong opinions about drainage. |
| **The Bell Country** | The settlement he hauled water for. It was founded and lost by other people; chapter 15 is its collapse seen from the bottom. |
| **Mother Furnace** | A god invented by committee in an afternoon, for morale. He was in the room, holding something. He thought they were assigning chores. Still worshipped. |
| **Ais** | The apprentice the book is for. Named rarely. Chapter 20 is addressed to her. |
| **T.** | The editor, two generations later. Reveres him. Never met him. |

### Grief

Chapter 16 kills Vera Ott. **The cheerfulness does not crack.** He reports her
death as plainly as a broken pump and moves to the next practical point. The
reader does the grieving, because he will not. This holds for the whole book:
there is no chapter in which he becomes a different man.

---

## 4. Accuracy discipline

The premise collapses if the advice is wrong.

- **No invented numbers.** Treatment ratios, tourniquet placement, water and
  calorie minimums, food-preservation safety, fuel storage life come from
  established real-world guidance or they do not appear. A sentence loses its
  figure rather than gaining a stretched citation.
- Contested guidance takes the conservative position and says why.
- Uncertain means vaguer, not wronger.
- `notes/accuracy-log.md` records the real-world basis for every load-bearing
  claim, with an honest confidence tag.
- **His obliviousness never touches the technique.** He misses significance,
  never steps.

### Content boundaries

Off the page regardless of framing:

1. Weapons and explosives manufacture.
2. Operationalized coercive-control technique.

Chapters 15 and 18 handle cults from the inside, as failure modes to recognize.
In the redesign he is a better witness than a leader would be: he saw the
machinery from underneath, without the vocabulary to name it, which is how most
people meet it.

---

## 5. Illustrations

Generated later via nano banana. The style guide, slot placement and manifest
pipeline are built now, because consistency is decided by the style guide and
not by the generator.

### Style DNA

Two-ink civil-defense manual: flat black line plus one rust-orange spot colour,
paper grain, no gradients, no rendered lighting, rubbery cartoon figures with
bean-shaped bodies and heavy outlines. A boxed figure in a printed manual,
never bleed-to-edge. No background scenery unless a slot asks for it.

### Two classes

- **Plates** teach. Numbered callouts in the image, labels in the caption,
  correct technique. Reviewed against the accuracy log exactly as prose is.
- **Gags** (`class: gag`; "marginalia" in prose) are never load-bearing. In the
  redesign they carry much of the comedy: him under a motorcycle, him facing
  the wrong way, him holding something during a historic moment.

Budget ~3 per chapter, roughly 1 plate and 2 gags, ~60 total.

### Consistency

`notes/illustration-style.md` holds the fixed prompt preamble, the palette, the
do-not list, and the character and object sheets. Characters stay
silhouette-identifiable. **The narrator's sheet changes in the redesign:** he is
cheerful, slightly battered, frequently in the background or underneath
something, and his face is still not the subject.

### Placeholders

Every slot is written into the manuscript as an `ILLO` comment block carrying
its own prompt, followed immediately by its image link. `prompt:` must be a
single line or use indented continuations — never a YAML block scalar.
`scripts/collect_illos.py` extracts them to `notes/illustration-manifest.json`.

**The prose stands alone.** Every chapter reads correctly with zero images.

---

## 6. Repository layout

```
survival_guide/
  README.md
  docs/superpowers/specs/2026-11-17-long-after-design.md
  docs/superpowers/plans/2026-11-17-long-after.md
  manuscript/
    00-front-matter.md
    01-triage.md … 20-teaching.md
    99-appendices.md
  notes/
    style-guide.md            voice rules, apparatus template
    continuity.md             cast, factions, gods, timeline, Rule ledger, debts
    accuracy-log.md           real-world basis per load-bearing claim
    illustration-style.md     preamble, palette, character sheets
    illustration-manifest.json  generated
    manuscript-order.txt      the authoritative chapter list
    forbidden-terms.txt
  illustrations/              empty until generation
  scripts/                    illo_blocks.py, lint_manuscript.py, collect_illos.py
  tests/
```

---

## 7. Workflow

1. Reference documents before chapters. The voice and cast are decided once,
   in writing, then obeyed.
2. Chapters in order. One commit each. Anything a later chapter needs goes into
   `notes/continuity.md` **in the same commit**, never into a report.
3. Review checkpoint at the end of each Part.

### Definition of done

- 20 chapters plus front and back matter, 45,000–55,000 words.
- Every chapter carries all five apparatus elements.
- Every load-bearing claim has an accuracy-log entry.
- Every chapter has its illustration slots placed with prompts written.
- `notes/illustration-manifest.json` generates cleanly.
- The book reads correctly with zero images present.
- No chapter in which the narrator becomes a different man.

Illustration generation is out of scope until nano banana is connected.
