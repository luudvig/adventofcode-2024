#!/usr/bin/env python3

with open('input') as f:
    map = [int(d) for d in f.read().rstrip()]

new_map = []

i2 = 0
for i, d in enumerate(map):
    if i % 2 == 0:
        new_map.extend([i2] * d)
        i2 += 1
    else:
        new_map.extend(['.'] * d)


i = 0
while i < len(new_map):
    if new_map[i] == '.':
        e = new_map.pop()
        while e == '.':
             e = new_map.pop()
        try:
            new_map[i] = e
        except IndexError:
            new_map.append(e)
    i += 1

sum = 0
for i, d in enumerate(new_map):
    sum += i * d

print(sum)