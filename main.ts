// news-image-01 entry (Node 22, standard library only).
// The image is entry.png beside this file: a front-page-style montage of
// Friday 13 November 2026 — Nvidia CEO Huang resigns, tankers hit by mines
// in Hormuz, peace talks, a drone strike on a Russian warship, Iran's radar
// claim in Bahrain, the FBI's $400M N. Korea hack, the Microsoft 365 outage
// and Kane's record 126th cap — with a footer on the record deportations.
// The program copies it to /output/entry.png. Deterministic: same bytes
// every run. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
// No network, no randomness: the shipped PNG is copied verbatim, so the
// two grader runs always produce identical bytes.
const source = new URL('./entry.png', import.meta.url);
copyFileSync(source, join(outDir, 'entry.png'));
