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
        antinodes.add(positions[i])

        for j in range(i + 1, n):
            y, x = positions[i][0], positions[i][1]
            dy, dx = positions[j][0] - y, positions[j][1] - x

            while 0 <= y - dy < len(map) and 0 <= x - dx < len(map[0]):
                y, x = y - dy, x - dx
                antinodes.add((y, x))

            while 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]):
                y, x = y + dy, x + dx
                antinodes.add((y, x))

print(len(antinodes))