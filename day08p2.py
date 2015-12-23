#!/usr/bin/env python

with open('input/day08.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

code_length = 0
encoded_length = 0

for line in data:
    code_length += len(line)

    encsize = 2   # Two outer double quotes
    escaped = False
    for char in line:
        if char == '"':
            encsize += 2
        elif char == '\\':
            encsize += 2
        else:
            encsize += 1

    encoded_length += encsize

print encoded_length - code_length
