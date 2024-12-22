#!/usr/bin/env python3

class Mem():
    def __init__(b, pos, len):
        b.pos, b.len = pos, len
    def val(b):
        return (2*b.pos + b.len-1) * b.len // 2

with open('input') as file:
    map, mem, pos = tuple(int(d) for d in file.read().rstrip()), [], 0

for d in map:
    mem += [Mem(pos, d)]
    pos += d

for used in mem[::-2]:
    for free in mem[1::2]:
        if free.pos <= used.pos and free.len >= used.len:
            used.pos  = free.pos
            free.pos += used.len
            free.len -= used.len

checksum = (i * m.val() for i, m in enumerate(mem[::2]))

print(sum(checksum))