#!/usr/bin/env python

min_gifts = 29000000
houses = [0 for x in xrange(min_gifts/10 + 1)]

for elf in xrange(1, min_gifts/10 + 1):
    for house in xrange(elf, min_gifts/10 + 1, elf):
        houses[house] += elf * 10

for house_num, house in enumerate(houses):
    if house >= min_gifts:
        break

print house_num
