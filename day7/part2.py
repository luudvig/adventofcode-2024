#!/usr/bin/env python3

with open('input') as f:
    equations, total = tuple([int(n.rstrip(':')) for n in l.split()] for l in f), 0

def generate_expressions(numbers, i=0, expression=[]):
    if i == len(numbers) - 1:
        yield expression + [numbers[i]]
        return
    for op in ('+', '*', '|'):
        yield from generate_expressions(numbers, i + 1, expression + [numbers[i]] + [op])

for eq in equations:
    for expr in generate_expressions(eq[1:]):
        for i in range(1, len(expr) - 1):
            match expr[i]:
                case '+':
                    expr[i + 1] = expr[i - 1] + expr[i + 1]
                case '*':
                    expr[i + 1] = expr[i - 1] * expr[i + 1]
                case '|':
                    expr[i + 1] = int(f'{expr[i - 1]}{expr[i + 1]}')
        if eq[0] == expr[-1]:
            total += expr[-1]
            break

print(total)