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

splitters = []

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '^':
            splitters.append((x, y))


print(splitters)

for y, row in enumerate(grid):
    print(row)
    s = list(filterfalse(lambda x: x[1] != y, splitters))
    print(s)
    print("______")

