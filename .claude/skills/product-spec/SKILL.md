---
name: product-spec
description: |
  Product specification for a new feature or a change in what the user sees: picks at most five
  product questions for the owner, each with a recommendation, writes work/{feature}/spec.md, and
  checks it from the implementer's side. Use when the owner wants a new feature, asks to think a
  feature through or agree on what to build, or describes a product idea with open points, before
  any technical design.
---

# Product spec

The owner decides product; you decide everything technical. A spec fixes what the user gets so
the implementation needs no further product questions.

## 1. Gather

Read the product context in `project-knowledge` (`project.md`, product rules in `patterns.md`).
Facts there are hypotheses unless marked confirmed; a feature that depends on one confirms it
through a question. List every open point in the request.

## 2. Sort the open points

- **Technical** (storage, architecture, libraries, how to compute something): decide yourself and
  record it as an assumption. Never ask the owner.
- **Minor product gaps** where a sensible default exists and changing it later is cheap: take the
  default and list it under assumptions in the spec.
- **Product questions:** what remains. Rank by impact on the user times uncertainty. Ask at most
  five; drop the rest to assumptions.

## 3. Ask

All questions in one message, numbered, highest impact first, in Russian and in the owner's
terms, without technical vocabulary. End the message with: «Можно ответить „по рекомендациям“ или
назвать только пункты, где вы не согласны». Each question has:

- **Суть:** the question itself, one sentence.
- **Почему важно:** what depends on it.
- **Варианты:** two or three concrete options.
- **Рекомендация:** the option you recommend and why.
- **Что изменится для пользователя:** how each option looks to the user.

If the request has no product questions left after sorting, say so and go straight to the spec.

## 4. Write `work/{feature}/spec.md`

In Russian, addressed to the owner:

```markdown
# <Фича>

## Зачем
Проблема пользователя и ожидаемый эффект.

## Что видит пользователь
Сценарии по шагам, включая пустое состояние, прерывания и отказы, которые пользователь может
встретить.

## Критерии приёмки
Проверяемые утверждения: что должно происходить и как это проверить.

## Не входит
Что явно не делаем в этой фиче.

## Решения владельца
Вопрос → ответ, дата.

## Допущения
Принятые по умолчанию продуктовые решения; владелец может изменить любое.
```

## 5. Check from the implementer's side

Run `reviewer` in spec mode on the spec. Fix what it finds: one round, a second only on the
changed parts. A finding that needs a product choice becomes a question to the owner within the
five-question limit, or an assumption.

## 6. Hand over

Give the owner a short Russian summary: what will be built, decisions taken, assumptions. The
technical brief follows with the `engineering-design` skill.
