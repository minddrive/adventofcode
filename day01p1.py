#!/usr/bin/env python

with open('input/day01.txt') as fh:
    data = fh.read()

floor = 0

for char in data:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    else:
        raise RuntimeError('Bad character!')

print floor
