#!/usr/bin/env python

import random
import re


with open('input/day19.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

molecule = data[-1]
data = data[:-2]   # Remove blank line and molecule

pat = re.compile('(\w+) => (\w+)')
transforms = list()

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    transforms.append((m.group(1), m.group(2)))

steps = 0
mol = molecule

while mol != 'e':
    start = mol

    for frm, to in transforms:
        while to in mol:
            steps += mol.count(to)
            mol = mol.replace(to, frm)

    if start == mol:  # No progress, try again
        random.shuffle(transforms)
        mol = molecule
        steps = 0

print steps
