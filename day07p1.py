#!/usr/bin/env python

import re


# Global dict (I know, I know..)
wires = dict()


class CircuitNode(object):
    oper = None
    value = None
    final_value = None
    left = None
    right = None

    def __init__(self, name, **kwargs):
        self.name = name

        if 'oper' in kwargs:
            self.oper = kwargs['oper']

            if self.oper == 'NOT':
                try:
                    self.right = kwargs['right']
                except KeyError:
                    raise RuntimeError('Missing right node for NOT')
            else:
                try:
                    self.left = kwargs['left']
                    self.right = kwargs['right']
                except KeyError as exc:
                    raise RuntimeError('Missing %s node for %s'
                                       % (exc, self.oper))
        elif 'value' in kwargs:
            self.value = kwargs['value']
        else:
            raise RuntimeError('Malformed data for circuit node')

    def __repr__(self):
        if self.value:
            return '<Wire "%s": Value="%s">' % (self.name, self.value)
        else:   # self.oper must exist
            return '<Wire "%s": Oper="%s" Left="%r" Right="%r">' \
                % (self.name, self.oper, self.left, self.right)

    def calculate(self):
        # Short-circuit already calculated nodes
        if self.final_value:
            return self.final_value

        if self.value:
            try:
                result = int(self.value)
            except ValueError:
                result = wires[self.value].calculate()
        else:   # self.oper must exist
            if self.left:   # Need to check for case of NOT
                try:
                    left_operand = int(self.left)
                except ValueError:
                    left_operand = wires[self.left].calculate()

            try:
                right_operand = int(self.right)
            except ValueError:
                right_operand = wires[self.right].calculate()

            if self.oper == 'NOT':
                result = ~right_operand
            elif self.oper == 'AND':
                result = left_operand & right_operand
            elif self.oper == 'OR':
                result = left_operand | right_operand
            elif self.oper == 'LSHIFT':
                result = left_operand << right_operand
            elif self.oper == 'RSHIFT':
                result = left_operand >> right_operand

        self.final_value = result
        return result


with open('input/day07.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

pat1 = re.compile(r'(\w+) -> (\w+)')
pat2 = re.compile(r'(\w+) (\w+) (\w+) -> (\w+)')
pat3 = re.compile(r'(NOT) (\w+) -> (\w+)')

for line in data:
    m = re.match(pat1, line)
    if m:
        name = m.group(2)
        wires[name] = CircuitNode(name, value=m.group(1))
        continue

    m = re.match(pat2, line)
    if m:
        name = m.group(4)
        oper = m.group(2)
        wires[name] = CircuitNode(
            name, oper=oper, left=m.group(1), right=m.group(3)
        )
        continue

    m = re.match(pat3, line)
    if m:
        name = m.group(3)
        oper = m.group(1)
        wires[name] = CircuitNode(name, oper=oper, right=m.group(2))
        continue
    else:
        raise RuntimeError('Bad or malformed line')

print wires['a'].calculate()
