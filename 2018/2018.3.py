with open('2018 input') as file:
    claims = [line.strip().split(" ") for line in file]

grid = []

for y in range(1000):
    row = []
    for x in range(1000):
        row.append([y, x, 0])
    grid.append(row)

for claim in claims:

    claim.pop(1)
    id = claim.pop(0)

    x,y = list(map(int, claim[0][:-1].split(",")))
    width, height = list(map(int, claim[1].split("x")))
    for yi in range(y, y+height):
        for xi in range(x, x+width):
            grid[yi][xi][2] += 1

c = 0

for row in grid:
    for lattice in row:
        if lattice[2] > 1:
            c += 1

print(f"Part 1: {c}")