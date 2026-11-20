from collections import defaultdict
from itertools import combinations as comb

with open('2024 input') as file:
    grid = [list(line.strip()) for line in file]

symbols = defaultdict(list)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != '.':
            symbols[grid[y][x]].append((x, y))

maxx, maxy = len(grid[0])-1, len(grid)-1
antinodes = []
for freq, locs in symbols.items():
    pairs = list(comb(locs, 2))
    for pair in pairs:
        (x1, y1), (x2, y2) = pair
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        #8 cases

        #case 1: pair 1 is upleft from pair 2
        if x1 < x2 and y1 < y2:
            a1 = (x1-dx, y1-dy)
            a2 = (x2+dx, y2+dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 2: pair 1 is directly above pair 2:
        elif x1 == x2 and y1 < y2:
            a1 = (x1, y1-dy)
            a2 = (x2, y1+dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 3: pair 1 is upright from pair 2
        elif x1 > x2 and y1 < y2:
            a1 = (x1+dx, y1-dy)
            a2 = (x2-dx, y2+dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 4: pair 1 is directly right from pair 2
        elif x1 > x2 and y1 == y2:
            a1 = (x1+dx, y1)
            a2 = (x2-dx, y2)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 5: pair1 is downright from pair 2
        elif x1 > x2 and y1 > y2:
            a1 = (x1+dx, y1+dy)
            a2 = (x2-dx, y2-dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 6: pair1 is directly below pair 2
        elif x1 == x2 and y1 > y2:
            a1 = (x1, y1+dy)
            a2 = (x2, y2-dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 7: pair 1 is downleft from pair 2
        elif x1 < x2 and y1 > y2:
            a1 = (x1-dx, y1+dy)
            a2 = (x2+dx, y1-dy)
            antinodes.append(a1)
            antinodes.append(a2)

        #case 8: pair 1 is directly left from pair 2
        elif x1 < x2 and y1 == y2:
            a1 = (x1-dx, y1)
            a2 = (x2+dx, y2)
            antinodes.append(a1)
            antinodes.append(a2)

accantinodes = []
for node in antinodes:
    if 0 <= node[0] <= maxx and 0 <= node[1] <= maxy:
        accantinodes.append(node)

print(f"Part 1: {len(set(accantinodes))}")
antinodes = []
accantinodes = []
for freq, locs in symbols.items():
    pairs = list(comb(locs, 2))
    for pair in pairs:
        (x1, y1), (x2, y2) = pair
        dx = abs(x2-x1)
        dy = abs(y2-y1)

        antinodes.append((x1, y1))
        antinodes.append((x2, y2))
        # case 1: pair 1 is upleft from pair 2
        if x1 < x2 and y1 < y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 -= dx
                y1 -= dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 += dx
                y2 += dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 2: pair 1 is directly above pair 2:
        elif x1 == x2 and y1 < y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 -= dx
                y1 -= dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 += dx
                y2 += dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 3: pair 1 is upright from pair 2
        elif x1 > x2 and y1 < y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 += dx
                y1 -= dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 -= dx
                y2 += dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 4: pair 1 is directly right from pair 2
        elif x1 > x2 and y1 == y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 += dx
                y1 -= dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 -= dx
                y2 -= dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 5: pair1 is downright from pair 2
        elif x1 > x2 and y1 > y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 += dx
                y1 += dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 -= dx
                y2 -= dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 6: pair1 is directly below pair 2
        elif x1 == x2 and y1 > y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 -= dx
                y1 += dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 += dx
                y2 -= dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 7: pair 1 is downleft from pair 2
        elif x1 < x2 and y1 > y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 -= dx
                y1 += dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 += dx
                y2 -= dy
                a2 = (x2, y2)
                antinodes.append(a2)

        # case 8: pair 1 is directly left from pair 2
        elif x1 < x2 and y1 == y2:
            while 0 <= x1 <= maxx and 0 <= y1 <= maxy:
                x1 -= dx
                y1 -= dy
                a1 = (x1, y1)
                antinodes.append(a1)
            while 0 <= x2 <= maxx and 0 <= y2 <= maxy:
                x2 += dx
                y2 += dy
                a2 = (x2, y2)
                antinodes.append(a2)


accantinodes = []
for node in antinodes:
    if 0 <= node[0] <= maxx and 0 <= node[1] <= maxy:
        accantinodes.append(node)

print(f"Part 2: {len(set(accantinodes))}")