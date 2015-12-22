#!/usr/bin/env python

with open('input/day02.txt') as fh:
    data = fh.read()

packages = data.split('\n')[:-1]
ribbon = 0

for package in packages:
    dims = [ int(x) for x in package.split('x') ]
    dims.sort()

    areas = [ dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2] ]

    perim = 2 * (dims[0] + dims[1])
    bow = (dims[0] * dims[1] * dims[2])
    ribbon += (perim + bow)

print ribbon
