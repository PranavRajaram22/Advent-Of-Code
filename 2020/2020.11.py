from copy import deepcopy

with open('2020 input') as file:
    grid = [list(line.strip()) for line in file]

while True:
    newgrid = deepcopy(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pos = grid[y][x]
            if pos == 'L':
                occ = 0
                for dy in range(y-1, y+2):
                    for dx in range(x-1, x+2):
                        if not(dy==y and dx==x) and 0 <= dy < len(grid) and 0 <= dx < len(grid[0]):
                            if grid[dy][dx] == '#':
                                occ += 1

                if occ == 0:
                    newgrid[y][x] = '#'

            elif pos == '#':
                occ = 0
                for dy in range(y-1, y+2):
                    for dx in range(x-1, x+2):
                        if not(dy==y and dx==x) and 0 <= dy < len(grid) and 0 <= dx < len(grid[0]):
                            if grid[dy][dx] == '#':
                                occ += 1

                if occ >= 4:
                    newgrid[y][x] = 'L'


    if newgrid == grid:
        c = 0
        for row in newgrid:
            c += row.count("#")
        print(f"Part 1: {c}")
        break

    grid = newgrid