#!/usr/bin/env python3

from re import finditer

with open('input') as f:
    do, instructions, result = True, f.read(), 0

for m in finditer(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)', instructions):
    if m.group(0).startswith('do'):
        do = m.group(0) == 'do()'
    elif do:
        result += int(m.group(1)) * int(m.group(2))

print(result)