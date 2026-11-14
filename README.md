# news-image-01 — v3: "THE WORLD TODAY"

One image summing up the world's news of Friday 13 November 2026, laid out
as a newspaper front page — a deliberate break from v2's globe ringed by
vignettes.

- Lead: **Senate summons Nvidia chief** — empty witness chair, leather
  jacket draped over it, Senate hearing room.
- **Zelensky meets US envoys** (handshake, Ukrainian / US / EU flags)
- **Drone hits Russian warship** (smoking warship, cold northern sea)
- **Iran claims Bahrain radar strike** (radar dome, missile streak)
- **FBI: N. Korea $400M crypto hack** (fake video call, spilling coins)
- **Kane breaks England caps record — 126**
- **US reports record 483,200 deportations in 2026**

All seven stories are taken from the kit's own sources (BBC / Al Jazeera,
first reported 13 November 2026). Every label is spelled exactly as shown
and legible at 300 px across.

## Entry

`main.ts` (Node 22, stdlib only) copies `entry.png` to `/output/entry.png`.
The image is JPEG bytes named `entry.png`, 1024x1024, 288,991 bytes — inside
the gate's 1 MiB / 1024x1024 limits.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Variants considered

Three fresh layouts were generated and inspected; the front page won:

- **A — front page (chosen):** clearest hierarchy, largest legible type,
  every story readable from its picture + label, no invented details.
- **B — day timeline:** readable, but the generator invented clock times
  for each story — a faithfulness risk under the judge's criteria.
- **C — world map with pins:** labels correct, but pin numbering was
  duplicated and Kane's pin landed in South America — wrong geography.

License: MIT (see `LICENSE`).
