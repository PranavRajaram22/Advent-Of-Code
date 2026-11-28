import math
from collections import defaultdict

with open('2018 input') as file:
    coords = [list(map(int, line.strip().split(", "))) for line in file]

whitelist = coords

miny = min([coord[1] for coord in coords])
minx = min([coord[0] for coord in coords])
maxy = max([coord[1] for coord in coords])
maxx = max([coord[0] for coord in coords])

grid = []

for y in range(0, maxy+1):
    row = []
    for x in range(0, maxx+1):
        row.append('.')

    grid.append(row)

dist = defaultdict(list)


def manDist(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))


bounds = []

for x in range(len(grid[0])):
    bounds.append((x, 0))
    bounds.append((x, len(grid)-1))

for y in range(len(grid)):
    bounds.append((0, y))
    bounds.append((len(grid[0])-1, y))


infs = set()
for bound in bounds:
    mindist = math.inf
    mindistcoord = (0, 0)
    for coord in coords:
        dist = manDist(bound, coord)
        if dist < mindist:
            mindist = dist
            mindistcoord = tuple(coord)

    infs.add(mindistcoord)


notinfs = []
for coord in coords:
    if tuple(coord) not in infs:
        notinfs.append(coord)

dists = defaultdict(int)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        mindist = math.inf
        mincoord = (0, 0)
        for coord in coords:
            dist = manDist((x, y), coord)
            if dist < mindist:
                mindist = dist
                mincoord = coord

        dists[tuple(mincoord)] += 1



notinfsdists = []
for coord in notinfs:
    notinfsdists.append(dists[tuple(coord)])

print(f"Part 1: {max(notinfsdists)}")


c = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        totaldist = 0
        for coord in coords:
            dist = manDist((x, y), coord)
            totaldist += dist
        if totaldist < 10000:
            c += 1

print(f"Part 2: {c}")