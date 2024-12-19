#!/usr/bin/env python3

with open('example') as f:
    blocks, map = [], tuple(int(d) for d in f.read().rstrip())

i, j = -1, 0
while i < len(map) - 1:
    i += 1
    if map[i] == 0:
        continue
    elif i % 2 == 0:
        blocks.append([j] * map[i])
        j += 1
    else:
        blocks.append(['.'] * map[i])

#print(blocks)

i, e = len(blocks), None
while i > 0:
    i -= 1
    if blocks[i][0] == '.':
        continue

    j = -1
    while j < len(blocks) - 1 and j < i:
        j += 1
        if blocks[j][0] != '.' or len(blocks[i]) > len(blocks[j]):
            continue
        ldiff = len(blocks[j]) - len(blocks[i])
        b1, b2 = blocks.pop(i), blocks.pop(j)
        if ldiff > 0:
            blocks.insert(j, ['.'] * ldiff)
        blocks.insert(j, b1)
        if i == len(blocks) - 1:
            blocks.insert(i + 1, ['.'] * len(b1))
        else:
            blocks.insert(i, ['.'] * len(b1))
        #i = len(blocks)
        i += 1
        break
    #print(blocks)

flat_blocks = tuple(b1 for b2 in blocks for b1 in b2)
#print(flat_blocks)

checksum = tuple(i * d for i, d in enumerate(flat_blocks) if d != '.')

print(sum(checksum))