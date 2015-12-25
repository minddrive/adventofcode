#!/usr/bin/env python

from copy import copy
from itertools import izip
from math import ceil


def tuple_add(tuple1, tuple2):
    return tuple(x + y for x, y in izip(tuple1, tuple2))


def hits_to_kill(attacker, defender):
    rel_damage = attacker['damage'] - defender['armor']
    if rel_damage < 1:
        rel_damage = 1

    return ceil(defender['hitpoints'] / float(rel_damage))


# tuple is (Cost, Damage, Armor)
weapons = [
    (8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0),
]
armor = [
    (0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5),
]
rings = [
    (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3),
]
rings_comb = [(0, 0, 0)] + rings

for idx in xrange(len(rings) - 1):
    for idx2 in xrange(idx + 1, len(rings)):
        rings_comb.append(tuple_add(rings[idx], rings[idx2]))

full_combs = list()

for weapon in weapons:
    for arm in armor:
        for ring in rings_comb:
            full_combs.append(
                tuple_add(tuple_add(weapon, arm), ring)
            )

# Yeah, not reading this in from data file...
boss = {
    'hitpoints': 103,
    'damage': 9,
    'armor': 2,
}
myself = {
    'hitpoints': 100,
    'damage': 0,
    'armor': 0,
}

max_cost = 0
for comb in full_combs:
    new_myself = copy(myself)
    new_myself['damage'] += comb[1]
    new_myself['armor'] += comb[2]

    if hits_to_kill(new_myself, boss) > hits_to_kill(boss, new_myself):
        if comb[0] > max_cost:
            max_cost = comb[0]

print max_cost
