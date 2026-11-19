# The Long After — Final Pass

Run 2026-11-18, against `docs/superpowers/specs/2026-11-17-long-after-design.md`'s
definition of done. Reference document; never linted, never published.

The governing instruction of this pass was **fix defects, do not improve
writing**. One defect was fixed. Everything else below is evidence.

---

## 1. The definition of done, line by line, with its evidence

| Spec line | Verdict | Evidence |
|-----------|---------|----------|
| 20 chapters plus front and back matter | **Met** | 22 files in `notes/manuscript-order.txt`, all present (the linter errors on a listed file that does not exist, and exits 0). H1s run `# Chapter 1:` to `# Chapter 20:` with no number missing or repeated; `00-front-matter.md` and `99-appendices.md` are the front and back matter. |
| 45,000–55,000 words | **Not met — 58,248 words, 3,248 over.** | Per-file counts in section 2, taken after `illo_blocks.strip_comments`. **Stated, not acted on.** No chapter is outside the hard 1,800–3,200 band. The overrun is the user's call; this pass changed nothing for word count and declined one otherwise-correct fix because it would have broken the band (section 5). |
| Every chapter carries all five apparatus elements | **Met** | `python3 scripts/lint_manuscript.py` → `Manuscript clean.`, exit 0. It checks the H1, the blockquote epigraph inside the first twelve lines, `## What It Costs You`, `## The Short Version` with 5–9 `- ` lines and nothing bulleted after it, the word band, the `## Chapter NN` accuracy heading, forbidden terms, ILLO block shape, duplicate ids, and every `Rule N` against the ledger. |
| Every load-bearing claim has an accuracy-log entry | **Met** | `notes/accuracy-log.md` carries `## Chapter 01` through `## Chapter 20` plus `## Appendices`, every one with entries: 16, 19, 29, 20, 28, 21, 15, 18, 16, 16, 19, 36, 30, 15, 12, 7, 7, 6, 8, 5 and 10 respectively. **No `_No entries yet._` remains anywhere** in `manuscript/` or `notes/` — the only occurrences of that string are in the log's own header, where it documents the convention, and in the plan. |
| Every chapter has its illustration slots placed with prompts | **Met** | 61 slots: three in each of nineteen chapters and four in chapter 18. All five keys present and non-empty in every block — the linter fails otherwise. Figure numerals ascend in document order in all 20 chapters, and no slot sits after `## The Short Version`. |
| `notes/illustration-manifest.json` generates cleanly | **Met** | `python3 scripts/collect_illos.py` → `Wrote 61 slot(s)`, exit 0, no hand-editing. |
| The book reads correctly with zero images present | **Met** | `illustrations/` does not exist, so no image resolves anywhere (see section 6). Three chapters read start to finish — 3 (Part I), 12 (Part III), 17 (Part V) — and no sentence in any of them depends on an image. Whole-book mechanical sweep for image-dependent prose (*see the figure*, *as drawn*, *above*, *below*, *opposite*, *overleaf*, *pictured*, *figure N*) outside image links: **zero hits in 22 files**. |
| No chapter in which the narrator becomes a different man | **Met** | Checked chapter by chapter against style-guide §4 and §9. The register holds across Vera Ott's death line (`16-grief.md:9`, one line, next sentence about a brake), across chapter 12's "more of the people I have liked" line, across chapter 17's handprint beat and its grave, and across chapter 20, which carries no recognition, no reckoning and no goodbye. 52 tests pass. |

## 2. The numbers

Comment-stripped, via `illo_blocks.strip_comments`.

| File | Words |
|------|-------|
| 00-front-matter.md | 703 |
| 01-triage.md | 2,449 |
| 02-run-or-dig-in.md | 2,623 |
| 03-body.md | 3,182 |
| 04-water.md | 2,730 |
| 05-weather.md | 2,682 |
| 06-food.md | 2,560 |
| 07-first-people.md | 2,658 |
| 08-gear.md | 2,754 |
| 09-scavenging.md | 2,691 |
| 10-machine.md | 2,555 |
| 11-voices.md | 2,561 |
| 12-rot.md | 3,194 |
| 13-growing.md | 3,198 |
| 14-economy.md | 2,857 |
| 15-groups.md | 2,957 |
| 16-grief.md | 2,737 |
| 17-silhouette.md | 2,766 |
| 18-gods.md | 3,042 |
| 19-holidays.md | 3,009 |
| 20-teaching.md | 2,856 |
| 99-appendices.md | 1,484 |
| **Total** | **58,248** |

**58,248 against a 45,000–55,000 target: 3,248 words over, or about six per
cent.** Every chapter is inside the enforced 1,800–3,200 band; the overrun is
the accumulation of the per-chapter overruns declared as they happened, each
recorded in `notes/continuity.md` with its reason. Nothing in this pass was changed for it.

## 3. The checks no tool makes

1. **Dark asides.** The brief's "exactly one per chapter" was **superseded by
   `notes/style-guide.md` §4**, which retired the budget outright: "There is no
   designated dark aside any more. There is no budget to spend and no trapdoor
   to open." The live test is register, not count, and some chapters carry a
   recorded second dark line on purpose (chapter 17's grave, logged in
   continuity). Every dark line checked against §4's four tests — same register
   as the practical sentences round it, serving technique rather than mood, the
   next sentence carrying on, the reader doing the grieving. All pass. Nothing
   changed.
2. **No winking.** Chapters 18 and 19 read in full against the settled test:
   *does the narrator hold the view this sentence expresses, and is there an
   addressee?* No sentence in either requires the author to step outside him.
   Chapter 18's riskiest lines are his own flat judgements (the broom, the
   four valleys, "I did not see why it mattered"); chapter 19's are his
   reasoning about boots and snow. T.'s beats have an addressee by design and
   are T.'s own views, which is not the narrator winking.
3. **The Ninth Hand.** Builds across 3 (the woman who moved his hand, Rule 7),
   4 (the water ceremony, the handprint, the cracked lid), 7 (the greased gate,
   two years, "it was not that bad"), 15 (the one exempt man, Rule 77), 17 (the
   handprint's origin and "Somebody started counting"), 18 (a god built on the
   same five things, and the broom). **Its leader is described nowhere.** The
   only agent named anywhere is "Somebody made different choices"
   (`18-gods.md:151`). No villain is supplied in any chapter, retrospectively
   or otherwise.
4. **Vera Ott.** `09-scavenging.md:9` (one clause), chapter 10 (her chapter,
   the only place she speaks), `16-grief.md:9` (one line). **Nothing after
   chapter 16** — no scene, no burial, no further mention. Verified by grep on
   both "Vera" and "Ott" across all 22 files.
5. **Ais.** Named once in the whole manuscript, in chapter 20's first sentence,
   and once by T. in the preface. Never before chapter 20.
6. **Rule contradictions.** All 37 ledger Rules (2 to 80) read against each
   other. **None contradicts another.** The four pairs that could have — 12
   against 26 (small first trade against never naming the first number), 55
   against the tools-are-capital position, 58 against the greens exception, 47
   against 35 — are each explicitly harmonised in the prose at the point of
   use, and 61 against 36 is resolved by the arranged-in-advance cover.
7. **Chapter openings.** All 20 name a specific person inside the opening,
   before the first `##`: Edda Mull, Halla Dorn, Isak Roon, Pell Hask, Marta
   Lunn, Arno Bligh, the permanently unnamed woman on the track (specific, and
   canon forbids naming her), Benno Kell, Vera Ott, Vera Ott, Ruda Vilk, Alma
   Dack, the Bellwright, Oren Tass, Hollis Dray, Vera Ott, Halla Dorn, Tobin
   Arr, Lise Hadden, Ais.

## 4. The four extra sweeps

**4a. Every cross-reference, opened and verified.** 102 `chapter N` references
and 138 `Rule N` citations enumerated mechanically and each target opened.
Every `Rule N` gloss in the manuscript matches its ledger row's advice; the
linter already guarantees the number exists, and this pass checked that the
words round it describe the same Rule. **One pointer was wrong without being
false and is fixed** (section 5). The other near-misses were checked and found
correct: chapter 9's pointer at chapter 5 for "basements, pits and tanks"
lands on chapter 5's enclosed-combustion material, which is what the sentence
is scoped to ("never below ground level with a lamp or a fire"); chapter 20's
boil-time passage quotes `04-water.md:141` and :103 verbatim; chapter 19's
three chapter-4 pointers, chapter 18's chapter-7 pointer at its `## Leaving`
section, and chapter 16's pointer at chapter 12's soap-at-the-latrine line all
describe what is actually there.

**4b. The apparatus against the voice rules.** All 61 captions, alt texts,
positions and callout numerals swept. Chapter 20's fix holds: Rule 80's body
statement at `20-teaching.md:170` is followed by nothing but
`## What It Costs You`, and `20-gag-02` sits well above it. No caption points
at the reader, announces a significance or ranks anything. The captions that
depict the editor's era rather than his own — `11-gag-01` (the framed list),
`12-gag-01` (the devotional poster) — are flat in his voice and name only what
he would name ("Six things, framed.", "Rule 2, and the bucket."), with the
figure doing the work and the man in it not looking up; they sit inside the
found-document frame chapter 20's review adjudicated. Two things were
considered and deliberately **not** changed, both recorded in section 5.

**4c. Principle against practice.** Chapter 19's defect is paid: the counting-
song claim is that "the rhyme tells you when one has gone missing", and the
verse two paragraphs later rhymes (*leap* / *keep*, lines 2 and 4); the prose
now says the song carries **three** things and carries the covering step
itself. Chapter 18's five design decisions were read against Mother Furnace as
built (chore, domain, demand, story, form) and against the three-beat origin
procedure as told — all five obeyed. Chapter 17's five criteria were read
against the Spoke's mark and against both plates: obeyed, with the one known
mismatch (chapter 18's icon against criterion 4) left alone deliberately, as
continuity requires. Chapter 15's five warning signs are consistent across the
prose, T.'s beat, the plate and the Short Version. Chapter 12's sanitation
rules are obeyed inside the chapter, including washing hands before wound care
and the deliberate distinction between never lifting off direct pressure and
the three-minute floor on a packed wound. No new instance of the shape found.

**4d. Every H1 against the contents line.** All 20 compared character for
character. **Nineteen match exactly.** Chapter 1 differs in one character and
the difference is a recorded deliberate choice, not a stale rename — see
section 5.

## 5. What this pass found and what it changed

**Changed: one defect.**

- **`manuscript/10-machine.md:135`** — the tires paragraph read "fine cracks
  that open when you flex the rubber hard; **chapter 8 is the long version of
  that test**." Chapter 8 carries no flex test. Its rubber paragraph
  (`08-gear.md:99`) is about ageing — hardening and cracking from air and
  light, store it slack, the tread tells you nothing — and the flex test is
  chapter 9's (`09-scavenging.md:135`), which attributes the ageing to chapter
  8 and states the test itself. `notes/accuracy-log.md:281` had it right all
  along ("re-cites chapter 08's logged rubber-ageing basis **and chapter 09's
  flex test**"); the prose pointer had bundled the two. It now reads "chapter 8
  is the long version of **what air and light do to rubber**", which is what
  chapter 8 is, and matches chapter 9's own wording. The test itself is stated
  in full in chapter 10, so no case lost coverage and §9.1 category 4 is not
  engaged. One clause in `notes/continuity.md`'s chapter-10 entry — the phrase
  "chapter 08's rubber-ageing flex test", which is where the conflation came
  from — is annotated with the correction so the next writer is not misled the
  same way.

**Found and deliberately not changed.**

- **The five shortened figure legends in chapters 12 and 13.** Five of 61
  slots print a shortened caption in the image link rather than the `caption:`
  value: `12-plate-01`, `12-gag-01`, `12-plate-02`, `13-plate-01`,
  `13-plate-02`. The other 56 print the caption verbatim, which is how a
  plate's orange callout numerals reach a legend. This was fixed, and the fix
  **broke the build**: the link text is prose to the word counter, and the full
  legends take chapter 12 to 3,254 and chapter 13 to 3,279, outside the
  1,800–3,200 band. Those two chapters are the book's longest, and that is
  evidently why their legends were shortened in the first place. The fix was
  reverted. Paying for it means cutting prose from the two chapters, which this
  pass is not authorised to do, so the choice belongs to the user: accept short
  legends in those two chapters, exempt image-link text from `WORDS` in
  `scripts/lint_manuscript.py`, or trim. **The three affected plates' callout
  content is carried in full in the prose either way**, so nothing is
  unteachable; it is the legend, not the instruction.
- **Chapter 1's title.** The contents line reads "Triage: Decide What You Are"
  (the spec's own wording, `2026-11-17-long-after-design.md:127`); the H1 reads
  `# Chapter 1: Triage — Decide What You Are`. The em dash is a recorded
  decision from task 9, taken because `# Chapter 1: Triage: Decide What You
  Are` double-colons. This is not the chapter-16/19 failure shape — no rename
  happened and nothing points at a dead name — and both forms name the same
  chapter unambiguously. Changing either side would overwrite a deliberate
  choice in approved front matter to buy one character of consistency.
- **`15-plate-02`'s caption**, which ends "RECOGNIZE, NOT BUILD." A capitalised
  instruction in a figure legend is the shape 4b hunts for, and it is also the
  book's only American spelling against four British "recognise"s in the prose.
  It is **briefed verbatim** (`task-23-brief.md`), logged in
  `notes/accuracy-log.md:413` as part of the chapter's coercion boundary, and
  it is a guardrail on the chapter's most dangerous material. Deliberate and
  logged beats consistent; not touched.
- **The preface's glass bulbs.** `00-front-matter.md:31` has T. say "Elsewhere
  he describes glass bulbs that made light out of wire. I have been shown the
  broken ones. I am prepared to believe in the glass." **No chapter contains a
  description of a light bulb.** The only "bulb" in the manuscript is chapter
  10's squeeze bulb. This is the same shape as the refrigerator debt — a
  preface promise about the body — and unlike that one it was never entered in
  continuity's debts section. It is largely self-paying: chapter 20 is titled
  "Teaching the Ones Who Never Saw a Lightbulb", and T.'s beat there
  (`20-teaching.md:124`) echoes the preface almost word for word. What is
  missing is a description in **his** voice. Every available fix is either new
  prose in an approved chapter or an edit to the preface, so this is reported
  rather than fixed.
- **Chapter 18, "And a hole, left in on purpose. They were the better part of
  an hour on it and ended by deciding to have none."** On the nearest-
  antecedent reading, "none" is the hole, which would contradict the design
  decision three lines above. The intended reading — no account of the cold
  country — is settled by the next sentence and by the Short Version's "one
  hole left in on purpose", and the joke is an hour's deliberation producing a
  blank. Correct as written; left alone.
- **Chapter 18's domain, "fire, metal and anything that has to be kept
  going"**, against the chapter's own insistence on a narrow domain, named
  twice. The sentence bounds itself in the same breath ("not the weather, the
  dead or the harvest"), which is the narrowness the cost section relies on.
  His framing, his limits; left alone.

**Nothing else was changed.** No sentence was rewritten for taste, no trim was
taken anywhere, and none of style-guide §9.1's five protected categories was
touched — no reason, no qualifier, no earned cost, no sole-coverage
cross-reference and no review-praised sentence. The sentences recorded as
protected in `notes/continuity.md` were read and left exactly as they stand:
"I was outside the door with two chairs." (16), the mark-on-a-person clause and
"Somebody started counting." (17), the broom sentence and "I painted the mark
and wrote the rest up that evening under *foundry rota*, the heading it is
still under in my book." (18), the two praised sentences in 19, and
"Four lines of mine against everything she has ever stood in front of. The
four lines lose." (20).

One fix on a book reviewed chapter by chapter is the expected result. A pass
that reported twenty improvements would have been a regression.

## 6. `illustrations/`

The directory **does not exist**, so every one of the 61 `![…](../illustrations/
<id>.png)` links resolves to nothing and the book is read exactly as the spec
requires it to survive being read. `.gitignore` carries `illustrations/*.png`,
and git cannot store an empty directory, so its absence is the normal state of
a fresh clone rather than a missing artefact. Image generation remains out of
scope; `notes/illustration-style.md` §8 is the procedure, and dropping files
into `illustrations/` is the only step it needs — no prose and no slot block
changes.

## 7. Two things later work must not disturb

Both of these protect the same line, the best one in the front matter: *"Two
pages have been torn out cleanly along a fold, by somebody with a steady hand
and a reason, and I would trade a year of grain to know which Rules a person
takes with them."*

1. **Every chapter owns at least one ledger Rule.** Verified: all twenty
   chapters appear in the `Chapter` column of `notes/continuity.md`'s ledger,
   and every chapter's epigraph is a Rule of its own. This is load-bearing and
   not bookkeeping. If any chapter owned no Rule, a reader could reason
   "nothing in Appendix A covers chapter N, so that is what the torn pages
   said" — and the standing prohibition is that the contents of the two torn
   Rules are never to be written down or narrowed, by anything, including a
   gap in the coverage. A future chapter, merge or renumbering that leaves a
   chapter Rule-less reconstructs by elimination what the book refuses to say.
2. **The two torn gaps in Appendix A.** Exactly two `[page torn]` marks, at
   39–41 and 78–79, both bare and unsigned, fixed in count by
   `00-front-matter.md:25` and now enforced by `tests/test_appendices.py` —
   which asserts no ledger row exists inside either gap, that the ledger holds
   thirty-seven rows with 80 the highest, that Appendix A transcribes the
   ledger verbatim and in order, and that the gap marks keep their counts (two
   torn, four forgotten) and stay unannotated. The destructive edit to guard
   against is not a stray citation — the linter catches those — but somebody
   adding a ledger row for a number inside a gap and writing it into the list,
   which would lint perfectly clean and now fails three tests. Do not close
   either gap, do not sign either mark, and do not let anything in the book
   narrow what either said.

---

Tooling at the close of this pass: `52 passed`, `Manuscript clean.` (exit 0),
`Wrote 61 slot(s)`.
