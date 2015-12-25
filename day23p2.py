#!/usr/bin/env python

import re


with open('input/day23.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat1 = re.compile('(hlf|tpl|inc) (a|b)')
pat2 = re.compile('(jmp) ([+-]\d+)')
pat3 = re.compile('(jie|jio) (a|b), ([+-]\d+)')
instructions = list()

for line in data:
    m = re.search(pat1, line)
    if m:
        instructions.append((m.group(1), m.group(2)))
        continue

    m = re.search(pat2, line)
    if m:
        instructions.append((m.group(1), int(m.group(2))))
        continue

    m = re.search(pat3, line)
    if m:
        instructions.append((m.group(1), m.group(2), int(m.group(3))))
        continue

    raise RuntimeError('Bad line!')

registers = {'a': 1, 'b': 0}
index = 0

while True:
    try:
        instruction = instructions[index]
    except IndexError:
        break

    oper = instruction[0]

    if oper == 'hlf':
        registers[instruction[1]] /= 2
        index += 1
    elif oper == 'tpl':
        registers[instruction[1]] *= 3
        index += 1
    elif oper == 'inc':
        registers[instruction[1]] += 1
        index += 1
    elif oper == 'jmp':
        index += instruction[1]
    elif oper == 'jie':
        if registers[instruction[1]] % 2 == 0:
            index += instruction[2]
        else:
            index += 1
    elif oper == 'jio':
        if registers[instruction[1]] == 1:
            index += instruction[2]
        else:
            index += 1
    else:
        raise RuntimeError('Should not get here!')

print registers['b']
