import re
from collections import defaultdict

with open('2023 input') as file:
    lines = [line.strip() for line in file]

pattern = re.compile(r'\d+')

nums = [] #(number, x, y)
symbols = []
gears = []
for y, line in enumerate(lines):
    x = 0
    while x < len(line):
        m = re.match(pattern, line[x:])
        if m:
            nums.append((m.group(0), x, y))
            x += len(m.group(0))
        else:
            if lines[y][x] != '.':
                symbols.append((x, y))
                if lines[y][x] == '*':
                    gears.append((x, y))
            x += 1

numgrid = defaultdict(list)

for numg in nums:
    num, x, y = numg
    size = len(num)
    invalidcoords = []
    for xi in range(x, x+size):
        invalidcoords.append((xi, y))
    for yi in range(y-1, y+2):
        for xi in range(x-1, x+size+1):
            if (xi, yi) not in invalidcoords and 0 <= xi < len(lines[0]) and 0 <= yi < len(lines):
                numgrid[(num, x, y)].append((xi, yi))

c = 0
for num, coords in numgrid.items():
    if any(i in symbols for i in coords):
        c += int(num[0])

print(f"Part 1: {c}")


c = 0
for gear in gears:
    adjnums = []
    for numg, coords in numgrid.items():
        if any(i == gear for i in coords):
            adjnums.append(int(numg[0]))

    if len(adjnums) == 2:
        c += adjnums[0]*adjnums[1]

print(f"Part 2: {c}")