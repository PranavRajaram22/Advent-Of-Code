from collections import defaultdict

with open('2021 input') as file:
    lines = [line.strip() for line in file]


coords = defaultdict(int)

for line in lines:
    line = line.split("->")
    for i, x in enumerate(line):
        line[i] = list(map(int, x.split(',')))
    x1, y1, x2, y2 = [*i for i in line]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2: #vertical

        for y in range(min(y1, y2), max(y1, y2)+1):
            coords[(x1, y)] += 1

    elif y1 == y2: #horizontal
        for x in range(min(x1, x2), max(x1, x2)+1):
            coords[(x, y1)] += 1


total = 0




for k, v in coords.items():
    if v > 1:
        total += 1

print(f'Part 1: {total}')

for line in lines:
    line = line.split("->")
    for i, x in enumerate(line):
        line[i] = list(map(int, x.split(',')))
    x1, y1, x2, y2 = [*i for i in line]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 != x2 and y1 != y2: #diagonal
        if y1 < y2:
            startx, starty = x1, y1
            endx, endy = x2, y2
        else:
            startx, starty = x2, y2
            endx, endy = x1, y1
        dx = (endx-startx)/(abs(endx - startx))
        dy = 1
        x, y = startx, starty
        coords[(x, y)] += 1

        while x != endx and y != endy:
            x += dx
            y += dy
            coords[(x, y)] += 1


total = 0
for k, v in coords.items():
    if v > 1:
        total += 1

print(f'Part 2: {total}')