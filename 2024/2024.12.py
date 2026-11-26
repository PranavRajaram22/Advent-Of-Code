from collections import defaultdict
from itertools import combinations


with open('2024 input') as file:
    grid = [list(line.strip()) for line in file]


def bfs(x, y, visited):
    adjcoords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    visited.add((x, y))
    for a in adjcoords:
        if a not in visited and 0 <= a[0] < len(grid[0]) and 0 <= a[1] < len(grid) and grid[a[1]][a[0]] == grid[y][x]:
            for z in bfs(*a, visited):
                visited.add(z)

    return visited


allvisited = set()
regions = defaultdict()
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if (x, y) not in allvisited:
            visited = set()
            visited = bfs(x, y, visited)
            visited = list(visited)
            visited = sorted(visited)
            regions[visited[0]] = visited
            for i in visited:
                allvisited.add(i)



def getArea(region): #region is a list
    return len(region)

def getPerimeter(region): #region is a list
    adj = []
    combs = list(combinations(region, 2))
    for pair in combs:
        (x1, y1), (x2, y2) = pair
        if x1 == x2 and abs(y1-y2) == 1:

            adj.append(pair)

        elif y1 == y2 and abs(x1-x2) == 1:
            adj.append(pair)

    p = len(region)*4
    for _ in adj:
        p -= 2
    return p


def getSides(region):
    corners = 0
    for cell in regions:



c = 0
for region in regions.values():
    c += getArea(region) * getPerimeter(region)

print(f"Part 1: {c}")

