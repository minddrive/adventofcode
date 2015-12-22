#!/usr/bin/env python

import re


with open('input/day05.txt') as fh:
    data = fh.read().split('\n')[:-1]

nice = 0

for string in data:
    m = re.findall('[aeiou]', string)

    if len(m) < 3:
        continue

    prev_char = string[0]
    for char in string[1:]:
        if prev_char == char:
            break
        else:
            prev_char = char
    else:
        continue

    if re.search('(ab|cd|pq|xy)', string):
        continue

    nice += 1

print nice
