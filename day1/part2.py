#!/usr/bin/env python3

with open('input') as f:
    left, right = zip(*(l.split() for l in f))

similarity = sum(int(l) * right.count(l) for l in left)

print(similarity)