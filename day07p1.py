#!/usr/bin/env python

import re


with open('input-day07.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat1 = re.compile(r'(\d+) -> (\w+)')
pat2 = re.compile(r'(\w+) (\w+) (\w+) -> (\w+)')
pat3 = re.compile(r'(NOT) (\w+) -> (\w+)')

wires = dict()

for line in data:
    m = re.match(pat1, line)
    if m:
        wires[m.group(2)] = int(m.group(1))
        continue

    m = re.match(pat2, line)
    if m:
        op = m.group(2)
        if op == 'AND':
            wires[m.group(4)] = wires[m.group(1)] & wires[m.group(3)]
        elif op == 'OR':
            wires[m.group(4)] = wires[m.group(1)] | wires[m.group(3)]
        elif op == 'LSHIFT':
            wires[m.group(4)] = wires[m.group(1)] << int(m.group(3))
        elif op == 'RSHIFT':
            wires[m.group(4)] = wires[m.group(1)] >> int(m.group(3))
        else:
            raise RuntimeError('Bad operator!')
        continue

    m = re.match(pat3, line)
    if m:
        wires[m.group(3)] = ~wires[m.group(2)]
        continue
    else:
        raise RuntimeError('Bad line!')

print wires['a']
