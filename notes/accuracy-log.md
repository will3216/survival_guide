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

- **Severe external bleeding is treated before airway and breathing.** Basis: the massive-haemorrhage-first ordering used in modern trauma teaching (the MARCH sequence) and in the public bleeding-control campaigns derived from it, on the grounds that uncontrolled external haemorrhage kills in minutes and is correctable with bare hands. Continues the ordering chapter 01 adopted. Confidence: conservative-choice.
- **Direct pressure done properly: locate the exact bleeding point; a cloth or dressing between hand and wound if one is to hand, bare hand if not; heel of the hand on that one spot with the second hand stacked on top, arms locked and shoulders over, so body weight does the work; press harder than feels comfortable; do not move the hand or the spot.** Basis: standard first-aid and bleeding-control teaching on firm, localised, continuous direct pressure; the stacked-hands, locked-arms, body-weight posture is how pressure is taught to be sustained without fatigue in first-aid and bleeding-control courses. Confidence: high.
- **Hold pressure continuously for ten minutes at least, timed, and never lift off to check; bleeding through the dressing is treated by adding more material on top rather than removing what is there.** Basis: standard guidance that clot formation takes several uninterrupted minutes and that intermittent release disrupts it; published first-aid instruction gives ten minutes of uninterrupted pressure as a working minimum for serious bleeding and instructs against removing a soaked dressing. The chapter takes the longer, more conservative hold and gives no upper figure. Confidence: conservative-choice.
- **Handover of pressure: the relieving pair of hands goes on top before the first pair comes away, so the site is never unpressed.** Basis: routine practice in first-aid and pre-hospital care for maintaining uninterrupted haemostatic pressure during changeover. Confidence: high.
- **Wound packing: for deep or junctional wounds (thigh, shoulder, armpit, groin, side of the neck), push dressing material into the wound down to the bleeding source, keep feeding it in until the cavity is full and tight, then hold firm pressure for a good three minutes without moving; leave the packing in place.** Basis: Stop the Bleed / tactical-casualty-care wound-packing instruction — pack gauze (haemostatic or plain) directly into the wound to the source, fill the cavity completely, then maintain at least three minutes of direct pressure, and do not remove the packing in the field. The chapter notes that most people under-pack, which is the documented common error. Confidence: high.
- **Do not pack wounds of the chest, abdomen or head.** Basis: standard wound-packing contraindication in bleeding-control teaching — these cavities offer no compressible base and packing risks further injury; such wounds are managed by other means and are beyond bare-hands care. Confidence: high.
- **Tourniquets are for limbs only — never the neck, shoulder or trunk — and are indicated when pressure will not hold the bleed, when the responder must move, or when casualties outnumber responders.** Basis: tourniquet doctrine in tactical and civilian bleeding-control guidance: tourniquets apply to extremity haemorrhage only, and are indicated for life-threatening limb bleeding that direct pressure cannot control or where tactical/resource constraints prevent sustained pressure. Junctional and truncal bleeding is explicitly not a tourniquet site. Confidence: high.
- **A manufactured windlass tourniquet is preferred; improvised tourniquets use a wide strap and a strong rod, never a cord or wire.** Basis: published guidance preferring commercially manufactured windlass tourniquets over improvised ones, and the long-standing instruction that an improvised tourniquet must be broad (narrow cord or wire concentrates pressure, damages tissue and often fails to occlude). Confidence: conservative-choice.
- **Placement: high and tight on the limb between wound and body, a few inches above the wound, higher acceptable, never over a joint; over skin or clothing either way.** Basis: standard tourniquet application guidance — placement proximal to the wound (commonly given as 2–3 inches / 5–8 cm above it, or high on the limb when the site is unclear), never across a joint because occlusion fails there. The chapter gives "a few inches" rather than a precise figure and states the conservative fallback (higher is acceptable, too low is not). Confidence: conservative-choice.
- **Tighten until the bleeding stops — that is the only endpoint; the pain is expected and is not a reason to loosen a turn. If bleeding continues, apply a second tourniquet immediately above the first rather than adjusting the first.** Basis: tourniquet guidance that the application endpoint is cessation of bleeding (and loss of distal pulse), that tourniquet pain is expected and routinely causes under-tightening, and that a second tourniquet placed side by side or just proximal to the first is the standard response to continued bleeding. Confidence: high.
- **Write the time of application down immediately — on the strap, on the skin, on a label, anywhere legible.** Basis: universal tourniquet practice — application time governs every subsequent clinical decision about the limb, and marking it on the device or the casualty is standard in both military and civilian protocols. Confidence: high.
- **The person who applied the tourniquet never loosens or removes it; if no one with greater capability exists, it stays on and the application time is handed over.** Basis: standard civilian and tactical guidance that a tourniquet applied for life-threatening haemorrhage should not be periodically released or removed by a lay responder, and that conversion or removal is a clinical decision. Periodic loosening — once taught — is specifically warned against. The chapter takes the strictest position available and explains why. Confidence: conservative-choice.
- **Airway and breathing come after haemorrhage control: ten seconds to assess for normal breathing; an occasional noisy gasp is not breathing.** Basis: resuscitation-council guidance on assessing breathing for no more than ten seconds and on agonal gasping being frequently mistaken for normal breathing. Confidence: high.
- **An unresponsive but normally breathing casualty is turned onto their side (recovery position) and monitored; this is done even where spinal injury is suspected, because airway obstruction is the more immediate threat.** Basis: first-aid and resuscitation guidance on the recovery position for unresponsive breathing casualties, and the standing principle that airway management takes precedence over spinal-motion restriction when the two conflict. Confidence: conservative-choice.
- **Not breathing normally: chest compressions, heel of the hand on the centre of the chest with the other on top, arms straight, hard and fast, allowing full chest recoil, at a rate between 100 and 120 per minute, continued until breathing returns, relief arrives, or the rescuer cannot continue.** Basis: current resuscitation-council and AHA basic-life-support guidance: compression rate 100–120 per minute, hand placement on the centre of the chest, full recoil between compressions. The 100–120 figure is a published guideline range and is the only numeric rate in the chapter. The chapter deliberately gives no depth figure and no compression-to-ventilation ratio. Confidence: high.
- **Remove only visible, reachable obstruction from the mouth; no blind finger sweeps.** Basis: long-standing first-aid instruction against blind finger sweeps, which can drive an obstruction further in. Confidence: high.
- **Shock recognition: pale, grey, clammy skin; cold hands; weak rapid pulse; rapid shallow breathing; thirst; nausea; restlessness and agitation progressing to quietness and confusion — deterioration in conscious level being the more serious sign.** Basis: standard first-aid and pre-hospital descriptions of hypovolaemic shock, including altered mental state (anxiety and restlessness progressing to confusion and unresponsiveness) as a late and serious sign. Confidence: high.
- **Shock treatment: treat the cause first (usually haemorrhage); lay the casualty flat and keep them still; insulate from the ground as well as covering them; nothing by mouth; loosen constrictive items other than a tourniquet; monitor and record changes.** Basis: first-aid shock management — control bleeding, keep the casualty lying down, warm and still, and withhold oral fluids because of the possibility of surgery and the risk of aspiration. Insulation from the ground reflects hypothermia-prevention practice, conductive loss to the ground exceeding convective loss to air. Confidence: high.
- **Leg elevation ("shock position") is deliberately not recommended, and the chapter says why.** Basis: current first-aid guidance has largely withdrawn routine passive leg raising for shock for want of outcome evidence, and resuscitation-council first-aid reviews treat it as of uncertain benefit. The chapter takes the conservative position of flat-and-still and states the reason in text rather than giving a contested manoeuvre. Confidence: conservative-choice.
- **Fractures: splint in the position found, without straightening, realigning, or replacing a protruding bone.** Basis: standard first-aid fracture management — immobilise in the position found, do not attempt reduction, do not push protruding bone back; realignment in the field risks neurovascular and soft-tissue injury. Confidence: high.
- **Immobilise the joint above and the joint below the fracture; pad generously; the splint must be rigid and long enough; secure above and below the break, never over it; firm but not tight.** Basis: standard splinting practice in first-aid and wilderness-medicine teaching — a splint must span and immobilise the joints proximal and distal to the injury, with padding and with ties placed away from the fracture site. Confidence: high.
- **Check circulation, sensation and movement distal to the splint before applying it, after applying it, and again later; cold, white, blue or numb tissue past the splint means loosen it at once.** Basis: standard first-aid and wilderness-medicine instruction to assess and re-assess distal circulation, sensation and movement (including capillary refill) before and after splinting, because a splint applied or swollen too tight can cause ischaemic injury. This is the chapter's one and only instruction to loosen anything. Confidence: high.
- **An open fracture is covered with the cleanest available material and the bleeding managed by pressure around rather than directly over the protruding bone.** Basis: standard first-aid management of open fractures — cover to reduce contamination, control bleeding with pressure applied around the wound, do not press on exposed bone. Confidence: high.
- **What cannot be fixed by hands: internal haemorrhage; a head injury that progressively deteriorates; abdominal injury. The signs given — worsening shock with no accounting wound, a rigid tender abdomen, truncal bruising; and for head injury a lucid interval followed by increasing drowsiness, vomiting, confusion, difficulty rousing, unequal pupils and worsening headache — identify conditions requiring surgical care.** Basis: standard trauma teaching. Internal haemorrhage is not amenable to external compression and requires surgical control. The described head-injury pattern is the classic deteriorating intracranial haemorrhage picture (including the "talk and deteriorate" course and pupillary asymmetry), for which the definitive treatment is neurosurgical decompression. Blunt or penetrating abdominal trauma likewise requires surgical management. The list is scoped to exactly these three and the chapter offers no technique for any of them. Confidence: high.
- **In the absence of surgical care, the remaining measures are warmth, insulation from the ground, presence, honesty and withholding oral intake — and reallocating effort to casualties who can be helped.** Basis: palliative and mass-casualty triage principle — where definitive care is unavailable, care becomes comfort care, and triage doctrine directs finite effort toward casualties whose outcome it can change. The chapter states this plainly and claims no treatment effect for it. Confidence: conservative-choice.

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
