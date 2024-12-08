#!/usr/bin/env python3

with open('input') as f:
    appearances, lines = 0, f.read().splitlines();

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c != 'X':
            continue
        for d in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
            if (0 <= y + d[0] < len(lines) and 0 <= x + d[1] < len(l) and lines[y + d[0]][x + d[1]] == 'M' and
                0 <= y + d[0] * 2 < len(lines) and 0 <= x + d[1] * 2 < len(l) and lines[y + d[0] * 2][x + d[1] * 2] == 'A' and
                0 <= y + d[0] * 3 < len(lines) and 0 <= x + d[1] * 3 < len(l) and lines[y + d[0] * 3][x + d[1] * 3] == 'S'):
                appearances += 1

print(appearances)