#!/usr/bin/env python

from itertools import combinations


with open('input/day17.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

containers = sorted([ int(x) for x in data ], reverse=True)
eggnog = 150

for idx in xrange(len(containers)):
    subcount = 0

    for comb in combinations(containers, idx):
        if sum(comb) == eggnog:
            subcount += 1

    if subcount > 0:
        break

print subcount
