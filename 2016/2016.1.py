from collections import deque

with open('2016 input') as file:
    directions = [line.strip() for line in file][0]

directions = directions.split(", ")

compass = deque(['N', 'E', 'S', 'W'])

x, y = 0, 0

visited = []

for dir in directions:
    cardinal, mag = dir[0], int(dir[1:])
    if cardinal == 'L':
        compass.rotate(1)
    else:
        compass.rotate(-1)

    cardinal = compass[0]

    if cardinal == 'N':
        for i in range(mag):
            y += 1
            visited.append((x, y))
    elif cardinal == 'E':
        for i in range(mag):
            x += 1
            visited.append((x, y))
    elif cardinal == 'S':
        for i in range(mag):
            y -= 1
            visited.append((x, y))
    elif cardinal == 'W':
        for i in range(mag):
            x -= 1
            visited.append((x, y))



print(f"Part 1: {abs(x) + abs(y)}")
for coord in visited:
    if visited.count(coord) >= 2:
        x, y = coord
        print(f"Part 2: {abs(x) + abs(y)}")
        break