#!/usr/bin/env python3

with open('input') as f:
    blocks, map = [], tuple(int(d) for d in f.read().rstrip())

i, j = -1, 0
while i < len(map) - 1:
    i += 1
    if not map[i]:
        continue
    elif i % 2 == 0:
        blocks.append(str(j) * map[i])
        j += 1
    else:
        blocks.append('.' * map[i])

i = len(blocks)
while i > 0:
    i -= 1

    if blocks[i][0] == '.':
        continue

    j = -1
    while j < i - 1:
        j += 1
        if blocks[j][0] != '.' or len(blocks[j]) < len(blocks[i]):
            continue
        b = blocks.pop(i)

        if i > 0 and blocks[i - 1][0] == '.' and i < len(blocks) and blocks[i][0] == '.':
            blocks[i - 1] = blocks[i - 1] + '.' * len(b) + blocks[i]
            blocks.pop(i)
        elif i > 0 and blocks[i - 1][0] == '.':
            blocks[i - 1] = blocks[i - 1] + '.' * len(b)
        elif i < len(blocks) and blocks[i][0] == '.':
            blocks[i] = blocks[i] + '.' * len(b)
        else:
            blocks.insert(i, '.' * len(b))

        if len(blocks[j]) == len(b):
            blocks.pop(j)
        else:
            blocks[j] = blocks[j][len(b):]
        blocks.insert(j, b)

        break

sum = 0
for i, b in enumerate(''.join(blocks)):
    if b != '.':
        sum += i * int(b)

print(sum)