from collections import deque
from itertools import combinations
from more_itertools import sliding_window
import shapely
from shapely import count_coordinates
from shapely.plotting import plot_polygon
import matplotlib.pyplot as plt

with open('2025 input') as file:
    lines = [list(map(int, line.strip().split(","))) for line in file]



pairs = list(combinations(lines,2))

maxarea = 0

for pair in pairs:
    (x1, y1), (x2, y2) = pair
    area = (abs(x2-x1)+1) * (abs(y2-y1)+1)

    maxarea = max(maxarea, area)

print(f"Part 1: {maxarea}")

lines.append(lines[0])
lines = tuple(map(tuple, lines))
shape = shapely.Polygon(lines)

maxarea = 0

for pair in pairs:
    (x1, y1), (x2, y2) = pair
    area = 0
    if x1 == x2 or y1 == y2:
        area = abs(x1-x2) + abs(y1-y2) + 1
        s = shapely.LineString([[x1, y1], [x2, y2]])
    else:
        area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
        s = shapely.box(x1, y1, x2, y2)


    if shape.contains(s):
        maxarea = max(maxarea, area)



print(f"Part 2: {maxarea}")