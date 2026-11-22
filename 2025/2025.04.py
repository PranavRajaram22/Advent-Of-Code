with open('2025 input') as file:
    grid = [line.strip() for line in file]

count = 0

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if grid[y][x] == '@':
            c = 0
            for yi in range(y-1, y+2):
                for xi in range(x-1, x+2):
                    if 0 <= xi < len(row) and 0 <= yi < len(grid) and not (xi == x and yi == y):
                        if grid[yi][xi] == '@':

                            c += 1


            if c < 4:
                count += 1


print(f"Part 1: {count}")


oldgrid = grid.copy()
while True:
    newgrid = []
    for y, row in enumerate(oldgrid):
        currrow = []
        for x, char in enumerate(row):
            if char == '.':
                currrow.append('.')

            else:
                c = 0
                for yi in range(y - 1, y + 2):
                    for xi in range(x - 1, x + 2):
                        if 0 <= xi < len(row) and 0 <= yi < len(oldgrid) and not (xi == x and yi == y):
                            if oldgrid[yi][xi] == '@':
                                c += 1

                if c >= 4:
                    currrow.append('@')
                else:
                    currrow.append('.')

        newgrid.append(currrow)
    if newgrid == oldgrid:
        break
    else:
        oldgrid = newgrid.copy()


total = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if grid[y][x] == '@' and newgrid[y][x] == '.':
            total += 1

print(f'Part 2: {total}')







