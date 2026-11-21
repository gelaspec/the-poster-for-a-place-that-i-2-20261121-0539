# FUNGARA — The Village on the Great Mushroom

[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/gelaspec/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/gelaspec/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for a place that does not exist: **FUNGARA**, the
village on the great mushroom.

- **The place:** one colossal glowing mushroom rises out of a misty
  forest, and a whole lantern-lit village — cottages, fences, warm
  windows — sits on its cap, under a violet aurora.
- **The promise:** arrive at dusk with a lantern, walk the mossy
  path past smaller glowing mushrooms and fireflies, and sleep above
  the forest floor while the sky ripples overhead.
- **The name:** FUNGARA is set into the picture in large cream serif
  type over the night sky, with one line beneath it — the village on
  the great mushroom. No quotes, no ratings, no other copy.

## How it was built

The poster is composed with PIL: an AI-generated night-forest scene
(which carries no text) plus PIL-rendered typography, so every letter
is spelled exactly and the title stays readable at thumbnail size.
`main.py` (Python 3, standard library only, no network) copies the
held image `poster.jpg` to `/output/entry.png`, deterministically —
two runs write byte-identical files.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.
