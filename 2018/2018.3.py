with open('2018 input') as file:
    claims = [line.strip().split(" ") for line in file]

grid = []

for y in range(1000):
    row = []
    for x in range(1000):
        row.append([y, x, []])
    grid.append(row)


ids = []
for claim in claims:

    claim.pop(1)
    id = int(claim.pop(0)[1:])
    ids.append(id)
    x,y = list(map(int, claim[0][:-1].split(",")))
    width, height = list(map(int, claim[1].split("x")))
    for yi in range(y, y+height):
        for xi in range(x, x+width):
            grid[yi][xi][2].append(id)

c = 0

for row in grid:
    for lattice in row:
        if len(lattice[2]) > 1:
            c += 1

print(f"Part 1: {c}")

whitelist = list(range(1, len(claims)+1))

for row in grid:
    for lattice in row:
        if len(lattice[2]) > 1:
            for id in lattice[2]:
                try:
                    whitelist.remove(id)
                except ValueError:
                    pass


print(f"Part 2: {whitelist[0]}")