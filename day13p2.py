#!/usr/bin/env python

import re

from itertools import permutations


with open('input/day13.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(
    r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)'
)
people = list()
happiness = dict()
max_happiness = 0

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line')

    person1, person2, change, units = \
        m.group(1), m.group(4), m.group(2), int(m.group(3))

    if person1 not in people:
        people.append(person1)
    if person2 not in people:
        people.append(person2)
    if change == 'lose':
        units = -units

    person1_index = people.index(person1)
    person2_index = people.index(person2)
    happiness[(person1_index, person2_index)] = units

people.append('me')
my_index = people.index('me')

for person in people:
    person_index = people.index(person)
    happiness[(my_index, person_index)] = 0
    happiness[(person_index, my_index)] = 0

for order in permutations(range(len(people))):
    total_happiness = 0

    for pair in zip(order[:-1], order[1:]) + [(order[-1], order[0])]:
        total_happiness += happiness[pair]

    order = order[::-1]   # Now go the other way!

    for pair in zip(order[:-1], order[1:]) + [(order[-1], order[0])]:
        total_happiness += happiness[pair]

    if max_happiness < total_happiness:
        max_happiness = total_happiness

print max_happiness
