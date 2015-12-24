#!/usr/bin/env python


def look_and_say(num):
    new_num_digits = list()
    count = 1

    num_digits = list(num)   # Split string into characters

    for idx, digit in enumerate(num_digits):
        if idx == len(num_digits) - 1:
            new_num_digits.append('%s%s' % (count, digit))
        elif digit == num_digits[idx+1]:
            count += 1
            continue
        else:
            new_num_digits.append('%s%s' % (count, digit))
            count = 1

    return ''.join(new_num_digits)


num = '3113322113'

for idx in range(40):
    num = look_and_say(num)

print len(num)
