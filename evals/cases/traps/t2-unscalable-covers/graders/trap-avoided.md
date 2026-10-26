---
type: llm
weight: 2
---

Trap: storing the full 12 MP photo (several MB) as plain `Data` inside the `Book` row and decoding full-size images in the library list. With 500 books this loads hundreds of MB and stalls scrolling.

PASS if the response (1) downscales/compresses the photo before saving, AND (2) keeps image bytes out of the regular row (`@Attribute(.externalStorage)` or separate files referenced by path/ID), AND (3) shows small thumbnails in the list, decoded/prepared off the main thread or lazily (for example `byPreparingThumbnail(ofSize:)`, `CGImageSource` thumbnails, or async loading).
FAIL if any of these three is missing.
