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

- **"Three minutes without air. Three hours without shelter... Three days without water. Three weeks without food" — presented explicitly as a mnemonic for the *order*, not a schedule.** Basis: the "rule of threes" as taught in wilderness first-aid and search-and-rescue instruction; it is a teaching aid for priority ordering, and published wilderness-medicine guidance stresses that actual survival times vary enormously with environment, exertion and individual condition. The chapter states the caveat in text. Confidence: vague-on-purpose.
- **Air is first; loss of breathing is a matter of minutes.** Basis: basic physiology — irreversible hypoxic brain injury begins within a few minutes of circulatory or respiratory arrest, which is why resuscitation guidance treats it as the most time-critical condition. Confidence: high.
- **"Cold and wet and windy can finish a healthy adult in well under three hours."** Basis: standard hypothermia guidance — wet clothing and wind dramatically increase conductive and convective heat loss, and cold-water immersion in particular can cause incapacitation and death far faster than three hours. The chapter deliberately takes the pessimistic side of the mnemonic. Confidence: conservative-choice.
- **"Heat and hard work can wreck you in well under three days" (water).** Basis: dehydration and heat-illness guidance — fluid loss through sweat under heat and exertion can produce incapacitating dehydration and heat stroke within a day or less; the three-day figure assumes temperate rest. Confidence: conservative-choice.
- **"You will be stupid and clumsy and bad-tempered long before you are starving."** Basis: starvation and semi-starvation research (notably the documented cognitive, emotional and physical effects of prolonged caloric restriction) showing marked degradation in concentration, mood, irritability and physical capacity well before life-threatening starvation. Confidence: high.
- **Acute stress narrows vision, degrades hearing and fine motor control, distorts time perception, and reduces the ability to compare options.** Basis: the acute stress (sympathetic/catecholamine) response, well documented in aviation, diving, law-enforcement and emergency-medicine incident analysis: perceptual narrowing ("tunnel vision"), auditory exclusion, loss of fine motor dexterity, time distortion, and reduced working-memory capacity for option generation. Confidence: high.
- **Countermeasure: prolonged exhalation (breathe out longer than in, roughly five breaths) reduces arousal.** Basis: slow, exhalation-weighted breathing increases parasympathetic (vagal) tone and lowers heart rate; used in clinical anxiety management and in operational stress-inoculation training. It reduces arousal; it does not eliminate it, and the chapter says so. Confidence: high.
- **Countermeasure: complete one small, concrete, ordered physical task, named aloud, before deciding anything.** Basis: the same principle underlying written emergency checklists and read-aloud procedures in aviation, surgery and fire service — externalising sequence offloads impaired working memory under high arousal; verbalising intended actions is standard crew-resource-management practice. Confidence: high.
- **"Am I bleeding?" is asked before airway/breathing.** Basis: this is a deliberate adoption of the trauma-care ordering used in modern tactical and civilian bleeding-control teaching (massive haemorrhage before airway — the MARCH sequence, and the public "stop the bleed" message), which prioritises life-threatening external haemorrhage because it kills in minutes and is correctable by direct pressure alone. Confidence: conservative-choice.
- **Treatment given: look as well as feel, press hard and directly with whatever is at hand, and do not repeatedly lift to check.** Basis: standard bleeding-control guidance — firm, continuous, direct pressure; intermittent release disrupts clot formation. The chapter gives no dosage, device or tourniquet instruction and defers to chapter 3. Confidence: high.
- **Injured people frequently do not notice their own injuries in the immediate aftermath.** Basis: well-documented stress-induced analgesia and attentional narrowing in acute trauma; self-check-after-the-fact is standard first-aid practice. Confidence: high.
- **Invisible indoor air hazards: anything burning or running in an enclosed space; headache, nausea and sleepiness that began and worsened indoors mean get out and stay out.** Basis: carbon monoxide poisoning guidance — CO is colourless and odourless, early symptoms are headache, nausea, dizziness and drowsiness, and the instruction is to move to fresh air and not re-enter. Confidence: high.
- **"Do not go down after someone who went down before you; a great many of the dead in enclosed spaces are the second person in."** Basis: confined-space entry safety guidance, which records that a large share of confined-space fatalities are would-be rescuers who entered unprotected. The chapter gives the conservative instruction (do not enter) rather than any rescue technique. Confidence: conservative-choice.
- **If people know roughly where you are, staying put and being findable is usually right; if nobody knows, nobody is coming.** Basis: search-and-rescue practice — a known last-seen point and a stationary subject enormously shorten searches, and lost-person guidance generally favours staying put and increasing visibility when a search is expected. Confidence: high.
- **A counted check in a fixed order beats an unstructured sweep (including headcounts).** Basis: standard practice in inventory, pre-flight and casualty accounting — ordered enumeration with a defined endpoint reduces omission errors, and expectation-driven scanning produces known miscounts. Confidence: high.

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
