#!/usr/bin/env python

import re


with open('input/day16.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(
    'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
)
results = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
aunt_sues = dict()

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    sue_number = int(m.group(1))

    memories = dict()
    memories[m.group(2)] = int(m.group(3))
    memories[m.group(4)] = int(m.group(5))
    memories[m.group(6)] = int(m.group(7))

    for item in results:
        if item not in memories:
            memories[item] = -1

    aunt_sues[sue_number] = memories

for item, value in results.iteritems():
    for sue_number, memories in aunt_sues.iteritems():
        if memories is None:
            continue

        if memories[item] != value and memories[item] != -1:
            aunt_sues[sue_number] = None   # Not the one!
            continue

remaining_sue = [
    sue_number for sue_number in aunt_sues
    if aunt_sues[sue_number] is not None
]
if len(remaining_sue) > 1:
    print 'Too many Sues left: %s!' % len(remaining_sue)
else:
    print remaining_sue[0]
