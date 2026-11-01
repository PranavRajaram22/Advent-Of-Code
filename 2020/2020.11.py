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


with open('2020 input') as file:
    grid = [list(line.strip()) for line in file]

while True:
    newgrid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pos = grid[y][x]
            occ = 0

            # going up
            dy = y-1
            while dy >= 0:
                if grid[dy][x] == 'L':
                    break
                elif grid[dy][x] == '#':
                    occ += 1
                    break
                dy -= 1


            # going down
            dy = y+1

            while dy < len(grid):
                if grid[dy][x] == 'L':
                    break
                elif grid[dy][x] == '#':
                    occ += 1
                    break
                dy += 1

            # going left

            dx = x-1

            while dx >= 0:
                if grid[y][dx] == 'L':
                    break
                elif grid[y][dx] == '#':
                    occ += 1
                    break
                dx -= 1

            # going right
            dx = x+1

            while dx < len(grid[0]):
                if grid[y][dx] == 'L':
                    break
                elif grid[y][dx] == '#':
                    occ += 1
                    break
                dx += 1

            # going upright:

            dy = y-1
            dx = x+1
            while dy >= 0 and dx < len(grid[0]):
                if grid[dy][dx] == 'L':
                    break
                elif grid[dy][dx] == '#':
                    occ += 1
                    break
                dy -= 1
                dx += 1

            # going downright
            dy = y+1
            dx = x+1
            while dy < len(grid) and dx < len(grid[0]):
                if grid[dy][dx] == 'L':
                    break
                elif grid[dy][dx] == '#':
                    occ += 1
                    break
                dy += 1
                dx += 1

            # going upleft

            dy = y-1
            dx = x-1
            while dy >= 0 and dx >= 0:
                if grid[dy][dx] == 'L':
                    break
                elif grid[dy][dx] == '#':
                    occ += 1
                    break
                dy -= 1
                dx -= 1

            # going downleft

            dy = y+1
            dx = x-1
            while dy < len(grid) and dx >= 0:
                if grid[dy][dx] == 'L':
                    break
                elif grid[dy][dx] == '#':
                    occ += 1
                    break
                dy += 1
                dx -= 1

            if pos == 'L':
                if occ == 0:
                    newgrid[y][x] = '#'

            elif pos == '#':
                if occ >= 5:
                    newgrid[y][x] = 'L'


    if newgrid == grid:
        c = 0
        for row in newgrid:
            c += row.count("#")
        print(f"Part 2: {c}")
        break

    grid = newgrid
