from functools import cache
from itertools import filterfalse

import pandas as pd

with open('2025 input') as file:
    grid = [list(line.strip()) for line in file]


beams = [grid[0].index("S")]


total = 0
for y, line in enumerate(grid):
    if line.count("^") > 0:
        newbeams = []
        for beam in beams:
            if line[beam] == '^':
                newbeams.append(beam-1)
                newbeams.append(beam+1)
                total += 1
            else:
                newbeams.append(beam)
        beams = newbeams
        beams = set(beams)


print(f"Part 1: {total}")


beams = []
for i in range(len(grid[0])):
    if grid[0][i] != 'S':
        beams.append(0)
    else:
        beams.append(1)


for y in range(1, len(grid)):
    for x, char in enumerate(grid[y]):
        if char == '^':
            beams[x-1] += beams[x]
            beams[x+1] += beams[x]
            beams[x] = 0


print(f'Part 2: {sum(beams)}')

