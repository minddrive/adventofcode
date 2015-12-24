#!/usr/bin/env python

import re


with open('input/day14.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat = re.compile(
    '(\w+) can fly (\d+) km/s for (\d+) seconds, '
    'but then must rest for (\d+) seconds.'
)
total_time = 2503
distances = list()

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    name, rate, fly_time, rest_time = \
        m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))

    fly_dist_period = rate * fly_time
    full_period_num = total_time / (fly_time + rest_time)
    final_period_time = total_time % (fly_time + rest_time)

    if final_period_time < fly_time:
        fly_dist_final = rate * final_period_time
    else:
        fly_dist_final = fly_dist_period

    fly_total_dist = \
        fly_dist_period * full_period_num + fly_dist_final

    print '%s flew %s km' % (name, fly_total_dist)
    distances.append(fly_total_dist)

print max(distances)
