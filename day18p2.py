#!/usr/bin/env python

def neighbor_count(grid, light_pos, state):
    row, col = light_pos
    lights_on = 0

    # Stuck corner lights
    if (row == 0 or row == 99) and (col == 0 or col == 99):
        return state

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue   # Don't count light itself

            x2 = x + row
            y2 = y + col
            if (x2 < 0 or x2 > 99 or y2 < 0 or y2 > 99):
                continue   # Out of bounds

            lights_on += grid[x2][y2]

    if state:
        if lights_on == 2 or lights_on == 3:
            return state
        else:
            return state ^ 1
    else:
        if lights_on == 3:
            return state ^ 1
        else:
            return state


def update_grid(grid):
    new_grid = [[0 for y in xrange(100)] for x in xrange(100)]

    for x in xrange(100):
        for y in xrange(100):
            new_grid[x][y] = neighbor_count(grid, (x, y), grid[x][y])

    return new_grid


with open('input/day18.txt') as fh:
    data = fh.read().rstrip('\n').split('\n')

light_grid = list()

for line in data:
    light_line = list()
    for char in line:
        if char == '.':
            light_line.append(0)
        elif char == '#':
            light_line.append(1)
        else:
            raise RuntimeError('Bad line!')

    light_grid.append(light_line)

# Corner lights stuck on
light_grid[0][0] = light_grid[0][99] = \
    light_grid[99][0] = light_grid[99][99] = 1

for x in xrange(100):
    light_grid = update_grid(light_grid)

print sum(sum(light_grid, []))
