import math

with open('2020 input') as file:
    grid = [line.strip() for line in file]

x, y = 0, 0

part1count = 0

while y < len(grid):
    if grid[y][x] == '#':
        part1count += 1
    y += 1
    x = (x+3)%len(grid[0])


print(f"Part 1: {part1count}")

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

trees_hit = []

for slope in slopes:
    x, y, = 0, 0
    count = 0

    dy, dx = slope

    while y < len(grid):
        if grid[y][x] == '#':
            count += 1
        y += dy
        x = (x + dx) % len(grid[0])

    trees_hit.append(count)

print(f"Part 2: {math.prod(trees_hit)}")


