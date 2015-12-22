#!/usr/bin/env python

with open('input/day03.txt') as fh:
    data = fh.read()

starting_location = (0, 0)
visited_locations = set((0, 0))
pos_change = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}

curr_pos = starting_location

for char in data:
    curr_pos = (curr_pos[0] + pos_change[char][0],
                curr_pos[1] + pos_change[char][1])
    visited_locations.add(curr_pos)

print len(visited_locations)
