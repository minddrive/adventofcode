#!/usr/bin/env python

with open('input/day03.txt') as fh:
    data = fh.read()

starting_location = (0, 0)
visited_locations = set(((0, 0),))
pos_change = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}

curr_santa_pos = starting_location
curr_robo_pos = starting_location

for idx, char in enumerate(data):
    if idx % 2 == 0:
        curr_santa_pos = (curr_santa_pos[0] + pos_change[char][0],
                          curr_santa_pos[1] + pos_change[char][1])
        visited_locations.add(curr_santa_pos)
    else:
        curr_robo_pos = (curr_robo_pos[0] + pos_change[char][0],
                         curr_robo_pos[1] + pos_change[char][1])
        visited_locations.add(curr_robo_pos)

print len(visited_locations)
