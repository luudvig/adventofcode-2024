#!/usr/bin/env python3

with open('input') as f:
    antennas, antinodes, map = {}, set(), f.read().splitlines()

for y, l in enumerate(map):
    for x, c in enumerate(l):
        if c != '.':
            antennas.setdefault(c, []).append((y, x))

for freq, positions in antennas.items():
    n = len(positions)
    for i in range(n):
        y1, x1 = positions[i]

        for j in range(i + 1, n):
            y2, x2 = positions[j]

            dy = y2 - y1
            dx = x2 - x1

            n1 = (y1 - dy, x1 - dx)
            n2 = (y2 + dy, x2 + dx)

            if 0 <= n1[0] < len(map) and 0 <= n1[1] < len(map[0]):
                antinodes.add(n1)
            if 0 <= n2[0] < len(map) and 0 <= n2[1] < len(map[0]):
                antinodes.add(n2)

print(len(antinodes))