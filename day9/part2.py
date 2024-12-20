#!/usr/bin/env python3

with open('input') as f:
    blocks, map = '', tuple(int(d) for d in f.read().rstrip())

i, j = -1, 0
while i < len(map) - 1:
    i += 1
    if map[i] == '0':
        continue
    elif i % 2 == 0:
        blocks += str(j) * map[i]
        j += 1
    else:
        blocks += '.' * map[i]

i = len(blocks)
while i > 0:
    i -= 1
    
    if blocks[i] == '.':
        continue

    b1_end = i + 1
    try:
        b1_beg = next(k for k in range(i, -1, -1) if blocks[k] != blocks[i]) + 1
    except StopIteration:
        b1_beg = 0

    i = b1_beg

    j = -1
    while j < i:
        j += 1

        if blocks[j] != '.':
            continue

        b2_beg = j
        try:
            b2_end = next(k for k in range(j, i) if blocks[k] != blocks[j])
        except StopIteration:
            b2_end = b1_beg

        j = b2_end

        if (d1 := b1_end - b1_beg) <= (d2 := b2_end - b2_beg):
            blocks = blocks[:b2_beg] + blocks[b1_beg:b1_end] + blocks[b2_end - (d2 - d1):]
            blocks = blocks[:b1_beg] + '.' * d1 + blocks[b1_end:]
            break

sum = 0
for i, b in enumerate(blocks):
    if b != '.':
        sum += int(b) * i

print(sum)