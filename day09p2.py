#!/usr/bin/env python

import re

from itertools import permutations


with open('input/day09.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(r'(\w+) to (\w+) = (\d+)')
cities = list()
distances = dict()
max_trip = 0

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line')

    start_dest, end_dest, distance = m.group(1), m.group(2), int(m.group(3))

    if start_dest not in cities:
        cities.append(start_dest)
    if end_dest not in cities:
        cities.append(end_dest)

    start_index = cities.index(start_dest)
    end_index = cities.index(end_dest)
    distances[(start_index, end_index)] = distance
    distances[(end_index, start_index)] = distance

for order in permutations(range(len(cities))):
    total_dist = 0

    for pair in zip(order[:-1], order[1:]):
        total_dist += distances[pair]

    if total_dist > max_trip:
        max_trip = total_dist

print max_trip
