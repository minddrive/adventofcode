#!/usr/bin/env python

min_gifts = 29000000
houses = [0 for x in xrange(min_gifts/11 + 2)]

for elf in xrange(1, min_gifts/11 + 2):
    for house in xrange(elf, min(50*elf + 1, min_gifts/11 + 2), elf):
        houses[house] += elf * 11

for house_num, house in enumerate(houses):
    if house >= min_gifts:
        break

print house_num
