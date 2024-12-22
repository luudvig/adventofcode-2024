#!/usr/bin/env python3

with open('input') as f:
    blocks, map = [], tuple(int(d) for d in f.read().rstrip())

i, j = 0, 0
while i < len(map):
    if i % 2 == 0:
        blocks.extend([j] * map[i])
        j += 1
    else:
        blocks.extend(['.'] * map[i])
    i += 1

i, e = -1, None
while i < len(blocks) - 1:
    i += 1
    if blocks[i] != '.':
        continue
    while True:
        e = blocks.pop()
        if e != '.':
            break
    if i < len(blocks):
        blocks.pop(i)
    blocks.insert(i, e)

checksum = (i * d for i, d in enumerate(blocks) if d != '.')

print(sum(checksum))