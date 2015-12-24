#!/usr/bin/env python

import re


class Reindeer(object):
    def __init__(self, rate, fly_time, rest_time):
        self.rate = rate
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.remaining_time = fly_time + rest_time
        self.distance = 0


with open('input/day14.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(
    '(\w+) can fly (\d+) km/s for (\d+) seconds, '
    'but then must rest for (\d+) seconds.'
)
total_time = 2503
reindeer = dict()
points = dict()

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    name, rate, fly_time, rest_time = \
        m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))

    reindeer[name] = Reindeer(rate, fly_time, rest_time)
    points[name] = 0

for second in xrange(1, total_time+1):
    for name, buck in reindeer.iteritems():
        if buck.remaining_time > buck.rest_time:
            buck.distance += buck.rate

        buck.remaining_time -= 1
        if buck.remaining_time == 0:
            buck.remaining_time = buck.fly_time + buck.rest_time

    max_dist = max([buck.distance for buck in reindeer.values()])
    for name, buck in reindeer.iteritems():
        if buck.distance == max_dist:
            points[name] += 1

print max(points.values())
