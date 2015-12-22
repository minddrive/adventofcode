#!/usr/bin/env python

import re


def lights_set(task, start, end):
    for row in xrange(start[0], end[0]+1):
        for col in xrange(start[1], end[1]+1):
            if task == 'turn on':
                light_grid[row][col] += 1
            elif task == 'turn off':
                if light_grid[row][col] > 0:
                    light_grid[row][col] -= 1
            else:   # toggle
                light_grid[row][col] += 2


with open('input/day06.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

light_grid = [[0 for x in xrange(1000)] for x in xrange(1000)]
pat = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

for line in data:
    m = re.match(pat, line)

    if m is None:
        raise RuntimeError('Bad line!')

    task = m.group(1)
    start = (int(m.group(2)), int(m.group(3)))
    end = (int(m.group(4)), int(m.group(5)))

    lights_set(task, start, end)

print sum([sum(x) for x in light_grid])
