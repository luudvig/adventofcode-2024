#!/usr/bin/env python3

with open('input') as f:
    reports = [tuple(int(r) for r in l.split()) for l in f]

def check_safe(r):
    for i in range(1, len(r)):
        if i == 1:
            incr = r[i - 1] < r[i]
        if (incr and 1 <= r[i] - r[i - 1] <= 3) or (not incr and 1 <= r[i - 1] - r[i] <= 3):
            continue
        return False
    else:
        return True

safe = tuple(r for r in reports if check_safe(r))

print(len(safe))