from copy import deepcopy

with open('2015 input') as file:
    mastergrid = [list(line.strip()) for line in file]



grid = deepcopy(mastergrid)
oldgrid = grid.copy()
newgrid = []
currrow = []
for _ in range(100): #change to 100 for actual input

    for y, row in enumerate(oldgrid):
        for x, char in enumerate(row):
            c = 0
            for yi in range(y-1, y+2):
                for xi in range(x-1, x+2):
                    if 0 <= xi < len(row) and 0 <= yi < len(oldgrid) and not(xi == x and yi == y):
                        if oldgrid[yi][xi] == '#':
                            c += 1

            if oldgrid[y][x] == '#':
                if c == 2 or c == 3:
                    currrow.append("#")
                else:
                    currrow.append(".")

            else:
                if c == 3:
                    currrow.append("#")
                else:
                    currrow.append('.')

        newgrid.append(currrow.copy())
        currrow = []
    oldgrid = newgrid.copy()
    newgrid = []


c = 0
for line in oldgrid:
    c += line.count("#")

print(f"Part 1: {c}")

grid = deepcopy(mastergrid)
oldgrid = deepcopy(grid)
newgrid = []
currrow = []

oldgrid[0][0] = '#'
oldgrid[len(oldgrid) - 1][0] = '#'
oldgrid[0][len(oldgrid[0]) - 1] = '#'
oldgrid[len(oldgrid) - 1][len(oldgrid[0]) - 1] = '#'
for _ in range(100): #change to 100 for actual input
    for y, row in enumerate(oldgrid):
        for x, char in enumerate(row):
            c = 0
            for yi in range(y-1, y+2):
                for xi in range(x-1, x+2):
                    if 0 <= xi < len(row) and 0 <= yi < len(oldgrid) and not(xi == x and yi == y):
                        if oldgrid[yi][xi] == '#':
                            c += 1

            if oldgrid[y][x] == '#':
                if c == 2 or c == 3:
                    currrow.append("#")
                else:
                    currrow.append(".")

            else:
                if c == 3:
                    currrow.append("#")
                else:
                    currrow.append('.')

        newgrid.append(currrow.copy())
        currrow = []
    newgrid[0][0] = '#'
    newgrid[len(newgrid)-1][0] = '#'
    newgrid[0][len(newgrid[0])-1] = '#'
    newgrid[len(newgrid)-1][len(newgrid[0])-1] = '#'
    oldgrid = newgrid.copy()
    newgrid = []

c = 0
for line in oldgrid:
    c += line.count("#")

print(f"Part 2: {c}")



