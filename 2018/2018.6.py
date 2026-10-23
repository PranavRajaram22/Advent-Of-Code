import math
from collections import defaultdict

with open('2018 input') as file:
    coords = [list(map(int, line.strip().split(", "))) for line in file]

print(coords)

whitelist = coords

miny = min([coord[1] for coord in coords])
minx = min([coord[0] for coord in coords])
maxy = max([coord[1] for coord in coords])
maxx = max([coord[0] for coord in coords])

print(maxx, maxy, minx, miny)

grid = []

for y in range(0, maxy+2):
    row = []
    for x in range(0, maxx+2):
        row.append('.')

    grid.append(row)

dist = defaultdict(list)


def manDist(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))


for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if [x,y] in coords:
            grid[y][x] = "#"

d = defaultdict(int)
for y, row in enumerate(grid):
    print(row)
    for x, lattice in enumerate(row):

        mindist = math.inf
        mincoord = None
        for coord in coords:
            coord = tuple(coord)
            dl = manDist(coord, [y,x])
            if mindist > dl:
                mindist = dl
                mincoord = coord

        d[mincoord] += 1

print(d)


