# UX Guidelines

- [Status](#status)
- [Interface Language](#interface-language)
- [Accessibility Baseline](#accessibility-baseline)
- [Design Source and Acceptance](#design-source-and-acceptance)
- [Tone of Voice](#tone-of-voice)
- [Slumpy Character](#slumpy-character)
- [Domain Glossary](#domain-glossary)

## Status

Text patterns, palette, and components are not designed yet; fill them from the design instead of
inventing them. Tone and character come from the draft `mvp.md` and are hypotheses.

---

## Interface Language

Russian only for now. All user-facing strings go through a String Catalog from the first screen
(ADR-0001), so adding a language later does not mean rewriting views.

---

## Accessibility Baseline

From the first screen (ADR-0001): Dynamic Type, VoiceOver labels, dark theme.

---

## Design Source and Acceptance

- Visual design comes from Claude Design as web mockups and a design system. The agent translates
  colors, type, and components to SwiftUI; Claude Design does not produce SwiftUI.
- Design-system constraints for iOS: system font, Dynamic Type scale, minimum tap target size,
  light and dark themes.
- The owner accepts simulator screenshots on iOS 18 and on the current iOS (two visual styles,
  see the Swift rule), not the source HTML.

---

## Tone of Voice

Hypothesis from `mvp.md`: calm, concrete, dry deadpan humor carried by Slumpy; informal "ты",
short phrases; no guilt or loss framing, never anything like "Серия сгорела!" or "+50 XP".

---

## Slumpy Character

Hypothesis from `mvp.md`: minimalist neutral face (simple shape, two dot eyes, a line mouth); mood
is "today"; reactions are deadpan and defined during design. Rendering is not chosen; a SwiftUI
prototype comes first.

---

## Domain Glossary

- **Сессия** — one timed reading session in either mode.
- **Книга в руках** — mode for paper books and e-readers; the phone lies face down.
- **Читаю с телефона** — mode for reading apps on the phone with other apps blocked.
- **Подглядывание** — an honest look at the phone mid-session; it does not reset the session.
- **Что читать дальше** — the user's own queue of next books, not recommendations.
- **Скрытая книга** — a book whose title friends cannot see; they see only the minutes.
- **Дуэль** — a reading challenge between friends with a stake and a loss rule.
- **Ставка** — the non-monetary stake of a duel.
