#!/usr/bin/env python3

with open('input') as f:
    left, right = zip(*(l.split() for l in f))

distances = [abs(int(l) - int(r)) for l, r in zip(sorted(left), sorted(right))]

print(sum(distances))