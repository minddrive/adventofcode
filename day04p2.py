#!/usr/bin/env python

import hashlib


secret = 'iwrupvqb'

num = 1

while True:
    new_secret = secret + str(num)
    m = hashlib.md5()
    m.update(new_secret)

    if m.hexdigest()[:6] == '000000':
        print num
        break

    num += 1
