#!/usr/bin/env python

import re


with open('input/day05.txt') as fh:
    data = fh.read().split('\n')[:-1]

nice = 0

for string in data:
    two_subs = [ string[m:m+2] for m in xrange(len(string)-1) ]

    if len(two_subs) == len(set(two_subs)):
        continue

    found = False
    for idx in xrange(len(two_subs)-2):
        for sub_idx in xrange(idx+2, len(two_subs)):
            if two_subs[idx] == two_subs[sub_idx]:
                found = True
                break

        if found:
            break
    else:
        continue

    skip_pairs = zip(string[:-2], string[2:])

    if len([x for x in skip_pairs if x[0] == x[1]]) == 0:
        continue

    nice += 1

print nice
