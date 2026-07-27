# FlexChallenge — Site Redesign Plan

## Diagnosis of the current site

Measured: 7,040px tall at 1440×900 — 7.8 viewports.

1. **Dead air.** Roughly a third of the scroll is empty cream. Phone mockups float in
   space with 200–300px of nothing above and below them. Screens 3, 4 and 6 are more
   than half blank.
2. **Motion that fires once and dies.** The only scroll behaviour is a single
   `translateY(28px)` fade per element, with a 1.5s failsafe that force-reveals
   everything. Once a section has entered, scrolling produces zero visual change —
   which is what reads as "the parallax timing is off." Nothing is scroll-*linked*;
   it's scroll-*triggered*, once.
3. **The product is never demonstrated.** Four static PNGs, tilted. A visitor cannot
   tell what logging a day actually feels like, what the calendar does, or what the
   stats give back.
4. **Copy is close but hedged.** "Goals need a finish line" is fine but abstract.
   Nothing speaks to the person who already knows the work is the price.

## Direction

Keep the editorial bones — cream paper, ink type, mono spec-sheet voice, volt accent.
They're differentiated and they suit a discipline brand. Fix the execution.

### 1. Contrast rhythm instead of one flat field
Alternate paper and ink sections. The app is a dark app; its screens sit natively on
ink and pop hard against cream. Alternating gives the scroll a pulse and makes each
section arrival feel like an event.

### 2. Pinned product canvas instead of parallax
The centrepiece is a sticky section: the phone pins in the viewport while copy panels
advance beside it and **the phone's screen content changes with scroll progress**.
Scroll always produces immediate, proportional visual change — the structural cure for
"blank for too long." This is the Apple/Linear/Vercel technique, not a lagging offset.

### 3. The app UI is rebuilt live, not screenshotted
The signature move. The app screens are recreated in HTML/CSS/SVG so they can animate:

- **Task list** — tasks check themselves off, the water ring fills 96 → 128 oz, the
  step counter ticks 8,432 → 10,000, rows strike through.
- **75-day calendar** — 75 tiles fill green day by day as you scroll. This single
  visual explains the entire product in three seconds.
- **Statistics** — completion ring draws to 97%, trend bars grow, counters count up.
- **Task-type rail** — each of the seven log types demonstrates itself in miniature.

Crisp at any DPI, a fraction of the payload of the PNGs, and it *moves*. The real
screenshots stay on the page as a credibility strip, so nothing is overclaimed.

### 4. Ambient motion so the page is never dead
Marquee proof bar, breathing phone, counters that count, a hero task list that loops a
completion. Movement without busy-ness: nothing bounces, nothing spins, everything
eases on the same curve.

### 5. Motion rules
- Entrances complete in 500–700ms on `cubic-bezier(0.16, 1, 0.3, 1)`.
- Elements start animating when 12% into the viewport, so they're already in motion on
  arrival rather than catching up late.
- Stagger caps at 60ms per item, 5 items max.
- Scroll-linked work runs in one shared rAF loop reading one cached scroll value.
- `prefers-reduced-motion` collapses everything to final state.

## Copy platform

**Audience:** people improving their lives who already accept that it costs work,
commitment and integrity. They are not looking to be hyped. They are looking to be
taken seriously.

**Voice:** plain, declarative, short sentences. Specific over emphatic. The mono type
carries a receipt/spec-sheet tone — the record of what you did.

**Banned:** crush, unlock, level up, beast mode, transform your life, journey (as a
noun), "no excuses," exclamation points, hype adjectives, fire emoji.

**Spine:** integrity is doing what you said you'd do when nobody is watching. A
challenge is a promise with a date on it. The app keeps the receipt.

| Section | Line |
|---|---|
| Hero | **Do what you said you'd do.** |
| Premise | **Forever is not a commitment. It's a wish.** |
| Sequence | **75 days. 75 decisions. One record.** |
| Stats | **Discipline is boring. The proof isn't.** |
| Manifesto | **Nobody is watching. That's the whole point.** |
| Close | **Day 1 is today.** |

## Page architecture

| # | Section | Field | Job |
|---|---|---|---|
| 00 | Sticky nav | ink/blur | Persistent CTA |
| 01 | Hero | ink | Claim + live app demo |
| 02 | Proof ticker | volt | Free / no account / no tracking |
| 03 | Premise | paper | Why a challenge beats a streak (animated diagram) |
| 04 | How it works | paper | Three steps, each with a mini live UI |
| 05 | **Pinned sequence** | ink | Log → Calendar → Stats → Media, phone pinned |
| 06 | Task types | paper | Seven log types, each self-demonstrating |
| 07 | Templates | ink | Start from a proven plan |
| 08 | Real screens | paper | Actual screenshots — credibility |
| 09 | Integrity | ink | The manifesto |
| 10 | Privacy | paper | No servers, no accounts |
| 11 | Download | volt/ink | Close |
| 12 | Footer | ink | Links |

## Work chunks

1. Direction + mockup of hero and one signature section
2. Design tokens, shell, sticky nav, hero with live app UI
3. Live animated app-UI components (task list, calendar, stats, task-type rail)
4. Pinned scroll sequence and section rhythm
5. Full copy rewrite
6. Motion system, performance, reduced-motion, a11y
7. Responsive QA at five widths + sub-page alignment + meta/OG
8. Commit, push, publish preview
