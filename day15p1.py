#!/usr/bin/env python

import re


def comb_sum(total):
    for x in xrange(0, total + 1):
        for y in xrange(0, total + 1 - x):
            for z in xrange(0, total + 1 - x - y):
                yield (x, y, z, total - x - y - z)


with open('input/day15.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(
    '(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), '
    'texture (-?\d+), calories (-?\d+)'
)
ingredients = list()
max_product = 0

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    ingredients.append(
        (int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
    )

for ratio in comb_sum(100):
    product = 1
    for idx in xrange(4):
        prop_list = [x[idx] for x in ingredients]
        total = sum(x * y for x, y in zip(ratio, prop_list))

        if total <= 0:
            product = 0
            break   # No good
        else:
            product *= total

    if product > max_product:
        max_product = product

print max_product
