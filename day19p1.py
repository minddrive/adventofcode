#!/usr/bin/env python

import re


# Snagged from Stackoverflow
def replace_ith_instance(string, pattern, new_str, i=None, pattern_flags=0):
    # If i is None - replacing last occurrence
    match_obj = re.finditer(r'{0}'.format(pattern), string,
                            flags=pattern_flags)
    matches = [item for item in match_obj]
    if i == None:
        i = len(matches)
    if len(matches) == 0 or len(matches) < i:
        return string
    match = matches[i - 1]
    match_start_index = match.start()
    match_len = len(match.group())

    return '{0}{1}{2}'.format(string[0:match_start_index], new_str,
                              string[match_start_index + match_len:])


with open('input/day19.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

molecule = data[-1]
data = data[:-2]   # Remove blank line and molecule

pat = re.compile('(\w+) => (\w+)')
transforms = list()
new_molecules = set()

for line in data:
    m = re.search(pat, line)
    if not m:
        raise RuntimeError('Bad line!')

    transforms.append((m.group(1), m.group(2)))

for start, end in transforms:
    for idx in xrange(1, len(re.findall(start, molecule)) + 1):
        new_molecules.add(replace_ith_instance(molecule, start, end, idx))

print len(new_molecules)
