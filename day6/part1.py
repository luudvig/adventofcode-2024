#!/usr/bin/env python3

with open('input') as f:
    map = tuple([c for c in l.rstrip()] for l in f)

def starting_position():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^':
                return y, x

(y, x), positions = starting_position(), set()

while 0 < y < len(map) - 1 and 0 < x < len(map[y]) - 1:
    direction = map[y][x]

    if ((direction == '^' and map[y - 1][x] == '#') or
        (direction == '>' and map[y][x + 1] == '#') or
        (direction == 'v' and map[y + 1][x] == '#') or
        (direction == '<' and map[y][x - 1] == '#')):
        map[y][x] = '>' if direction == '^' else 'v' if direction == '>' else '<' if direction == 'v' else '^'
        continue
    
    map[y][x] = '.'
    y, x = (y - 1, x) if direction == '^' else (y, x + 1) if direction == '>' else (y + 1, x) if direction == 'v' else (y, x - 1)
    map[y][x] = direction
    positions.add((y, x))

print(len(positions))