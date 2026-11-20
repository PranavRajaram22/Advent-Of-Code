from copy import deepcopy
from math import floor

with open('2024 input') as file:
    grid = [list(line.strip()) for line in file]

x, y, = 0, 0
guard = '^'
for yi, row in enumerate(grid):
    if '^' in row:
        y = yi
        x = row.index('^')


pos = [(x, y)]
while True:
    if guard == '^':
        if y >= 1:
            if grid[y-1][x] == '#':
                guard = '>'
            else:
                y -= 1
                pos.append((x, y))

        else:
            break

    elif guard == '>':
        if x < len(grid[0])-1:
            if grid[y][x+1] == '#':
                guard = 'v'
            else:
                x += 1
                pos.append((x, y))
        else:
            break

    elif guard == 'v':
        if y < len(grid)-1:
            if grid[y+1][x] == '#':
                guard = '<'
            else:
                y += 1
                pos.append((x, y))

        else:
            break

    elif guard == '<':
        if x >= 1:
            if grid[y][x-1] == '#':
                guard = "^"
            else:
                x -= 1
                pos.append((x, y))
        else:
            break



print(f'Part 1: {len(set(pos))}')

def run(grid):
    x, y, = 0, 0
    guard = '^'
    pos = [(x, y, guard)]
    for yi, row in enumerate(grid):
        if '^' in row:
            y = yi
            x = row.index('^')

    while True:
        if guard == '^':
            if y >= 1:
                if grid[y - 1][x] == '#':
                    guard = '>'
                else:
                    y -= 1
                    if (x, y, guard) in pos:
                        return True
                    else:
                        pos.append((x, y, guard))

            else:
                return False

        elif guard == '>':
            if x < len(grid[0]) - 1:
                if grid[y][x + 1] == '#':
                    guard = 'v'
                else:
                    x += 1
                    if (x, y, guard) in pos:
                        return True
                    else:
                        pos.append((x, y, guard))
            else:
                return False

        elif guard == 'v':
            if y < len(grid) - 1:
                if grid[y + 1][x] == '#':
                    guard = '<'
                else:
                    y += 1
                    if (x, y, guard) in pos:
                        return True
                    else:
                        pos.append((x, y, guard))

            else:
                return False

        elif guard == '<':
            if x >= 1:
                if grid[y][x - 1] == '#':
                    guard = "^"
                else:
                    x -= 1
                    if (x, y, guard) in pos:
                        return True
                    else:
                        pos.append((x, y, guard))
            else:
                return False

c = 0
allp = []
for i, p in enumerate(pos[1:]):
    g = deepcopy(grid)
    g[p[1]][p[0]] = '#'
    if run(g):
        allp.append(p)

print(f"Part 2: {len(set(allp))}")