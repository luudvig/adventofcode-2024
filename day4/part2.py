#!/usr/bin/env python3

with open('input') as f:
    appearances, letters, lines = 0, {'M', 'S'}, f.read().splitlines();

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c != 'A':
            continue
        if (0 <= y - 1 and 0 <= x - 1 and lines[y - 1][x - 1] in letters and
            y + 1 < len(lines) and x + 1 < len(l) and lines[y + 1][x + 1] in letters - {lines[y - 1][x - 1]} and
            0 <= y - 1 and x + 1 < len(l) and lines[y - 1][x + 1] in letters and
            y + 1 < len(lines) and 0 <= x - 1 and lines[y + 1][x - 1] in letters - {lines[y - 1][x + 1]}):
            appearances += 1

print(appearances)