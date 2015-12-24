#!/usr/bin/env python

import json


total = 0

def total_numbers_in_data(data):
    global total   # yeah, yeah...

    if isinstance(data, dict):
        if 'red' in data.values():
            return   # Skip the whole dict
        for key in data:
            total_numbers_in_data(data[key])
    elif isinstance(data, list):
        for ele in data:
            total_numbers_in_data(ele)
    elif isinstance(data, int):
        total += data


with open('input/day12.txt') as fh:
    data = json.loads(fh.read())

total_numbers_in_data(data)
print total
