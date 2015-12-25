#!/usr/bin/env python

from itertools import combinations


with open('input/day24.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

weights = [int(x) for x in data]
weights = sorted(weights, reverse=True)
total_weight = sum(weights)
part_weight = total_weight / 4

part_sum = 0
min_count = 0

for weight in weights:
    part_sum += weight
    min_count += 1
    if part_sum > part_weight:
        break

min_prod = 100000000000000000

while True:
    for comb in combinations(weights, min_count):
        if sum(comb) == part_weight:
            min_prod = min(min_prod, reduce(lambda x, y: x * y, comb))

    if min_prod != 100000000000000000:
        break
    else:
        min_count += 1

print min_prod
