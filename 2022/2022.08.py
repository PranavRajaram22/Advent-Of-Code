with open('2022 input') as file:
    grid = [list(map(int, list(line.strip()))) for line in file]




def isVisible(x, y):
    tree = grid[y][x]
    top, bottom, left, right = [], [], [], []

    for yi in range(y):
        if 0 <= yi < len(grid):
            top.append(grid[yi][x])


    for yi in range(y+1, len(grid)):
        if 0 <= yi < len(grid):
            bottom.append(grid[yi][x])


    for xi in range(x):
        if 0 <= xi < len(grid[0]):
            left.append(grid[y][xi])

    for xi in range(x+1, len(grid[0])):
        if 0 <= xi < len(grid):
            right.append(grid[y][xi])


    if any(i >= tree for i in top) and any(i >= tree for i in bottom) and any(i >= tree for i in left) and any(i >= tree for i in right):
        return False

    return True

c = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if isVisible(x, y):
            c += 1

print(f"Part 1: {c}")

def score(x, y):

    tree = grid[y][x]
    top, bottom, left, right = [], [], [], []

    for yi in range(y-1, -1, -1):
        if 0 <= yi < len(grid):
            top.append(grid[yi][x])
            if grid[yi][x] >= tree:
                break


    for yi in range(y+1, len(grid)):
        if 0 <= yi < len(grid):
            bottom.append(grid[yi][x])
            if grid[yi][x] >= tree:
                break


    for xi in range(x-1, -1, -1):
        if 0 <= xi < len(grid[0]):
            left.append(grid[y][xi])
            if grid[y][xi] >= tree:
                break

    for xi in range(x+1, len(grid[0])):
        if 0 <= xi < len(grid):
            right.append(grid[y][xi])
            if grid[y][xi] >= tree:
                break

    return len(left)*len(right)*len(top)*len(bottom)



maxscore = 0


for y in range(len(grid)):
    for x in range(len(grid[0])):
        maxscore = max(maxscore, score(x, y))


print(f"Part 2: {maxscore}")