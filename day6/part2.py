#!/usr/bin/env python3

with open('input') as f:
    map = tuple([c for c in l.rstrip()] for l in f)

def starting_position():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^':
                return y, x

positions, (start_y, start_x) = 0, starting_position()

for obstr_y in range(len(map)):
    for obstr_x in range(len(map[obstr_y])):
        if map[obstr_y][obstr_x] != '.':
            continue

        visited = {(start_y, start_x): map[start_y][start_x]}
        map[obstr_y][obstr_x], y, x = '#', start_y, start_x
        
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
            
            if (y, x) in visited and visited[(y, x)] == direction:
                positions += 1
                break
            
            map[y][x] = direction
            visited[(y, x)] = direction

        map[obstr_y][obstr_x], map[y][x] = '.' * 2
        map[start_y][start_x] = '^'

print(positions)