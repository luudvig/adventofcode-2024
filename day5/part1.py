#!/usr/bin/env python3

with open('input') as f:
    pages = f.read().split('\n\n', 1)

rules = set(pages[0].splitlines())
updates = tuple(u.split(',') for u in pages[1].splitlines())

def correct_middle_page(u):
    for i, n in enumerate(u):
        for j in range(i):
            if f'{n}|{u[j]}' in rules:
                return 0
        for j in range(i + 1, len(u)):
            if f'{u[j]}|{n}' in rules:
                return 0
    return int(u[len(u) // 2])

middles = tuple(correct_middle_page(u) for u in updates)

print(sum(middles))