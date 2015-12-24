#!/usr/bin/env python


alphabet = 'abcdefghijklmnopqrstuvwxyz'
rejected_letters = 'ilo'.split()
doubles = [x * 2 for x in alphabet]
triples = [
    ''.join(x) for x in zip(alphabet[:-2], alphabet[1:-1], alphabet[2:])
]
valid_triples = [
    x for x in triples if all(i not in x for i in rejected_letters)
]
ord_base = 97   # Only works with ASCII!


def good_password(password):
    if not any(triple in password for triple in valid_triples):
        return False

    if any(bad_letter in password for bad_letter in rejected_letters):
        return False

    if len([double for double in doubles if double in password]) < 2:
        return False

    return True


def bump_password(password):
    new_password = list()
    carry = False

    for idx, char in enumerate(reversed(password)):
        if idx == 0 or carry:
            new_char = chr((ord(char) - ord_base + 1) % 26 + ord_base)

            if new_char == 'a':
                carry = True
            else:
                carry = False

            new_password.append(new_char)
        else:
            new_password.append(char)

    return ''.join(reversed(new_password))


orig_password = 'hepxcrrq'
new_password = bump_password(orig_password)

while not good_password(new_password):
    new_password = bump_password(new_password)

# Damn, password expired, what's next?
new_password = bump_password(new_password)

while not good_password(new_password):
    new_password = bump_password(new_password)

print new_password
