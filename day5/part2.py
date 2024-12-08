#!/usr/bin/env python3

with open('input') as f:
    pages = f.read().split('\n\n', 1)

middles = []
rules = set(pages[0].splitlines())
updates = tuple(u.split(',') for u in pages[1].splitlines())

def correct_middle_page(u):
    for i, n in enumerate(u):
        for j in range(i):
            if f'{n}|{u[j]}' in rules:
                return 0, i, j
        for j in range(i + 1, len(u)):
            if f'{u[j]}|{n}' in rules:
                return 0, i, j
    return int(u[len(u) // 2]), i, j

for u in updates:
    corrected = False
    while (r := correct_middle_page(u))[0] == 0:
        u[r[1]], u[r[2]] = u[r[2]], u[r[1]]
        corrected = True
    if corrected:
        middles.append(r[0])

print(sum(middles))