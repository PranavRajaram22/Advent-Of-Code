from operator import truediv

with open('2021 input') as file:
    grid = [list(map(int, list(line.strip()))) for line in file]

total = 0

lowpointcoords = []
for y, row in enumerate(grid):
    for x, loc in enumerate(row):
        adjcoords = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
        adj = []
        for a in adjcoords:
            xi, yi = a
            if 0 <= xi < len(row) and 0 <= yi < len(grid): #valid coord
                adj.append(grid[yi][xi])

        if not any(i <= loc for i in adj):
            lowpointcoords.append((x, y))
            total += loc + 1


print(f"Part 1: {total}")


def bfs(x, y, visited):
    if grid[y][x] == 9:
        return visited
    else:
        visited.add((x, y))
        adjcoords = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
        for a in adjcoords:
            xi, yi = a
            if 0 <= xi < len(row) and 0 <= yi < len(grid) and (xi, yi) not in visited:  # valid coord
                bfs(xi, yi, visited)


basinsizes = []
for lp in lowpointcoords:
    visited = set()
    bfs(*lp, visited)
    basinsizes.append(len(visited))

basinsizes.sort(reverse=True)
print(f'Part 2: {basinsizes[0] * basinsizes[1] * basinsizes[2]}')

