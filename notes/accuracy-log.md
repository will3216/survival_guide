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
- **"You will be stupid and clumsy and bad-tempered a long time before you are starving."** Basis: starvation and semi-starvation research (notably the documented cognitive, emotional and physical effects of prolonged caloric restriction) showing marked degradation in concentration, mood, irritability and physical capacity well before life-threatening starvation. Confidence: high.
- **Acute stress narrows vision, degrades hearing and fine motor control, distorts time perception, and reduces the ability to compare options.** Basis: the acute stress (sympathetic/catecholamine) response, well documented in aviation, diving, law-enforcement and emergency-medicine incident analysis: perceptual narrowing ("tunnel vision"), auditory exclusion, loss of fine motor dexterity, time distortion, and reduced working-memory capacity for option generation. Confidence: high.
- **Countermeasure: prolonged exhalation (breathe out longer than in, roughly five breaths) reduces arousal.** Basis: slow, exhalation-weighted breathing increases parasympathetic (vagal) tone and lowers heart rate; used in clinical anxiety management and in operational stress-inoculation training. It reduces arousal; it does not eliminate it, and the chapter says so. Confidence: high.
- **Countermeasure: complete one small, concrete, ordered physical task, named aloud, before deciding anything.** Basis: the same principle underlying written emergency checklists and read-aloud procedures in aviation, surgery and fire service — externalising sequence offloads impaired working memory under high arousal; verbalising intended actions is standard crew-resource-management practice. Confidence: high.
- **"Am I bleeding?" is asked before airway/breathing.** Basis: this is a deliberate adoption of the trauma-care ordering used in modern tactical and civilian bleeding-control teaching (massive haemorrhage before airway — the MARCH sequence, and the public "stop the bleed" message), which prioritises life-threatening external haemorrhage because it kills in minutes and is correctable by direct pressure alone. Confidence: conservative-choice.
- **Treatment given: look as well as feel, press hard and directly with whatever is at hand, and do not repeatedly lift to check.** Basis: standard bleeding-control guidance — firm, continuous, direct pressure; intermittent release disrupts clot formation. The chapter gives no dosage, device or tourniquet instruction and defers to chapter 3. Confidence: high.
- **Injured people frequently do not notice their own injuries in the immediate aftermath.** Basis: well-documented stress-induced analgesia and attentional narrowing in acute trauma; self-check-after-the-fact is standard first-aid practice. Confidence: high.
- **Invisible indoor air hazards: anything burning or running in an enclosed space, a cellar, a stairwell, a shaft, a long-shut room; a thickening headache, sickness and sleepiness that began and worsened indoors mean get out into open air and stay out.** Basis: carbon monoxide poisoning guidance — CO is colourless and odourless, early symptoms are headache, nausea, dizziness and drowsiness, and the instruction is to move to fresh air and not re-enter. Confidence: high.
- **"Do not go down after somebody who went down before you. A great many of the dead in enclosed spaces are the second person in, and some of them are the third."** Basis: confined-space entry safety guidance, which records that a large share of confined-space fatalities are would-be rescuers who entered unprotected. The chapter gives the conservative instruction (do not enter) rather than any rescue technique. Confidence: conservative-choice.
- **If people know roughly where you are, staying put and being findable is usually right; if nobody knows, nobody is coming.** Basis: search-and-rescue practice — a known last-seen point and a stationary subject enormously shorten searches, and lost-person guidance generally favours staying put and increasing visibility when a search is expected. Confidence: high.
- **A systematic area search — dividing the ground into squares and finishing each one before starting the next — beats sweeping the same ground repeatedly.** Basis: standard search methodology (search-and-rescue sector/grid searching, and the same principle in evidence and underwater search): dividing an area into bounded segments and clearing each to a defined endpoint gives known coverage, whereas unstructured sweeping produces both repeated and missed ground. Described in the chapter's opening as how he searched the floor. Confidence: high.
- **A counted check in a fixed order beats an unstructured sweep (including headcounts).** Basis: standard practice in inventory, pre-flight and casualty accounting — ordered enumeration with a defined endpoint reduces omission errors, and expectation-driven scanning produces known miscounts. Confidence: high.

## Chapter 02

- **Stay put when the structure is sound, you have water or a certain way to get it, the hazard is outside and passing, and a route out still exists; leave when the structure is compromised, the hazard is present and worsening, or you have no water.** Basis: standard emergency-management guidance on shelter-in-place versus evacuation (civil-defence and national emergency-preparedness advice), which keys the decision to whether the hazard is inside or outside the building, whether the building remains habitable and structurally intact, and whether essential supplies — water above all — are available for the expected duration. Confidence: high.
- **The decision should be made early, stated aloud to another person, and acted on with daylight remaining.** Basis: emergency-management evacuation practice and crew-resource-management habit — pre-committing to a decision in front of others reduces the drift and re-litigation that produce late departures, and darkness degrades navigation, visibility and casualty handling. Confidence: conservative-choice.
- **Leaving late, not choosing wrong, is the dominant way people die of this decision.** Basis: post-incident analysis of wildfire and hurricane evacuations, which repeatedly finds that a large share of deaths occur among people who delayed and were then caught in the open or in vehicles on congested routes, rather than among people who sheltered in an appropriate structure. Late evacuation is recognised in wildfire guidance as more dangerous than either early evacuation or well-prepared sheltering. Confidence: high.
- **The two errors are asymmetric: leaving too early costs a wasted day and embarrassment, leaving too late can cost everything — so the decision should be biased toward going early.** Basis: standard asymmetric-risk reasoning as applied in official evacuation advice, which advises leaving early and explicitly accepts the cost of unnecessary evacuations against the cost of late ones. Confidence: conservative-choice.
- **Pre-set the departure trigger in advance as an observable condition rather than a feeling (e.g. "if the water reaches the step").** Basis: trigger-point planning, used in wildfire and flood evacuation planning and in incident-action planning generally — pre-defined, observable decision thresholds set while calm, because judgement degrades under acute stress (see chapter 01's entries on the acute stress response). Confidence: high.
- **Go-bag contents, in priority order: water, light, warmth, documents, medication, a knife; food last.** Basis: published emergency "go kit" / grab-bag guidance from national preparedness agencies and red-cross-type organisations, which consistently lists water, a torch with spare power, warm and dry layers, copies of identity and medical documents, prescription medication, and a multi-tool or knife, with non-perishable food included but ranked below water. The ordering also follows the chapter 01 priority order (air, shelter, water, food). Confidence: high.
- **"A litre of water weighs a kilogram" and water will be most of the bag's weight; household storage guidance is roughly four litres per person per day, and you will not carry three days of it.** Basis: the density of fresh water is 1 kg per litre by definition of the metric system; the storage figure corresponds to the widely published one-gallon-per-person-per-day household emergency recommendation (approximately 3.8 litres). The chapter states plainly that this quantity is not portable for multiple days and defers sourcing to the water chapter rather than inventing a carry figure. Confidence: high.
- **Carry water in more than one container.** Basis: standard redundancy practice in emergency kit design — a single container is a single point of failure (puncture, loss, contamination). Confidence: high.
- **Light: hands-free if possible, with a backup that does not share a battery type with the primary.** Basis: common practice in caving, mountain rescue and utility work — a head torch keeps hands available, and a second light on a different power source removes the shared failure mode of one dead battery type. Confidence: high.
- **Warmth: a dry spare insulating layer kept in a waterproof bag, plus a hat and a windproof layer; wet and wind are what kill.** Basis: hypothermia prevention guidance — wet clothing and wind greatly increase conductive and convective heat loss; keeping a dry insulating layer genuinely dry is standard mountain and cold-weather practice, and significant heat is lost from the uncovered head. Detailed treatment deferred to chapter 05. Confidence: high.
- **Medication: carry the written names of each medication, not just the pills, and rotate stock so it is not expired.** Basis: standard emergency-preparedness and travel-medicine advice — a written medication list (drug name, dose, frequency) lets any other provider continue treatment if containers are lost, and stored medication must be rotated before expiry. The chapter gives no doses, by design. Confidence: vague-on-purpose.
- **Documents: copy them and keep the copies separate from the originals.** Basis: routine emergency-preparedness guidance on identity, insurance and medical records; separation of copies is standard protection against a single loss event. Confidence: high.
- **Everyone's first bag is too heavy; test it by carrying it up and down one flight of stairs, and a load much past about a third of body weight degrades the carrier.** Basis: military and occupational load-carriage research, which documents progressive degradation of speed, agility, endurance and injury risk as load approaches and exceeds roughly 30 percent of body weight, and standard pack-fitting practice of loaded walk-testing before relying on a pack. The one-flight-of-stairs test is a practical proxy, not a measurement; the chapter presents it as such. Confidence: conservative-choice.
- **Heavy items (water) packed low and close to the back panel, not high and soft; "a bag that stays still weighs less than a bag that does not."** Basis: standard load-carriage and pack-packing practice — keeping dense mass low, close to the spine and near the body's centre of mass reduces torque, limits load sway and improves balance and economy of movement. Stated in the chapter's opening and shown in its go-bag plate. Confidence: high.
- **Roads are fast and watched; crowds and trouble concentrate at pinch points such as bridges, cuttings and junctions.** Basis: basic terrain and movement analysis used in land navigation and in evacuation traffic planning — transport corridors concentrate movement, and constriction points (bridges, defiles, interchanges) are documented congestion and interdiction locations in both evacuation studies and route-security practice. Confidence: high.
- **Water courses navigate themselves: following a drainage downhill reliably leads toward lower ground and habitation, and gives a landmark that can be relocated.** Basis: standard land-navigation technique — using a linear feature as a "handrail", and the long-established search-and-rescue and wilderness-navigation heuristic that drainages lead downhill toward larger watercourses and human settlement. Confidence: high.
- **But water routes are longer, wetter, sometimes impassable, and subject to rising levels; do not wade moving water whose bottom you cannot see, because moving water is stronger than it looks and will take your feet at shallow depth.** Basis: flood-safety and swiftwater-rescue guidance, which advises never entering moving floodwater on foot and notes that relatively shallow fast water is sufficient to knock an adult down, plus hypothermia risk from immersion. The chapter takes the conservative instruction (do not wade) rather than teaching a crossing technique. Confidence: conservative-choice.
- **Rule 11 — the second floor is not safer, it is only harder to leave: going up reduces you to one exit; most building drownings occur above the ground floor after an upward move with no second move; if you go up, know the way down and a second way out of the upper room.** Basis: flood-rescue and fire-escape guidance — flood advice warns specifically against entering an attic or closed upper space without a means of exit to the roof or outside, because rising water can trap occupants, and fire-escape planning requires two means of escape from every upper room. The chapter gives the conservative instruction and the two-exits requirement. Confidence: conservative-choice.
- **Leave written word of your departure: who you are, how many, when you left, and where you are headed.** Basis: search-and-rescue practice — a last-known point, party size, timing and intended route transform a search's size and duration; leaving an itinerary is standard advice for any party moving in remote or disrupted conditions. Follows directly from chapter 01's third question. Confidence: high.

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
