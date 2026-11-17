with open('2021 input') as file:
    grid = [list(map(int, list(line.strip()))) for line in file]

for row in grid:
    print(row)


def explode(x, y, visited):
    if grid[y][x] == 9:
        grid[y][x] = 0
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            if 0 <= xi < len(grid[0]) and 0 <= yi < len(grid) and (xi, yi) not in visited and not (xi == x and yi == y):
                grid[yi][xi] += 1

                visited.add((xi, yi))
                if grid[yi][xi] == 9:
                    grid[yi][xi] = 0
                    explode(xi, yi, set())



print("_______")
visited = set()
for y, row in enumerate(grid):
    for x, octo in enumerate(row):
        explode(x, y, visited)
        grid[y][x] += 1


for row in grid:
    print(row)
