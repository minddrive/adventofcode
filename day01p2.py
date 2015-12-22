#!/usr/bin/env python

with open('input/day01.txt') as fh:
    data = fh.read()

floor = 0

for position, char in enumerate(data, start=1):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    else:
        raise RuntimeError('Bad character!')

    if floor < 0:
        print position
        break
else:
    print 'Never reached basement!'
