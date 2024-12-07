#!/usr/bin/env python3

from re import finditer

with open('input') as f:
    instructions = f.read()

results = tuple(int(m.group(1)) * int(m.group(2)) for m in finditer(r'mul\((\d+),(\d+)\)', instructions))

print(sum(results))