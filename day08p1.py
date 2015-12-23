#!/usr/bin/env python

with open('input/day08.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

code_length = 0
memory_length = 0

for line in data:
    code_length += len(line)

    memsize = 0
    escaped = False
    hex_escape = 0
    for char in line[1:-1]:   # Strip enclosing double quotes
        if hex_escape > 0:
            if hex_escape == 1:
                memsize +=1
            hex_escape -= 1
            continue

        if escaped:
            escaped = False
            if char == 'x':
                hex_escape = 2
            else:
                memsize += 1
            continue

        if char == '\\' and not escaped:
            escaped = True
            continue
        else:
            memsize += 1

    memory_length += memsize

print code_length - memory_length
