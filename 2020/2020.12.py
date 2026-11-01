from collections import deque

compass = deque(['N', 'E', 'S', 'W'])

compass.rotate(-1)
#positive means last becomes first, first becomes second, etc. turning left
#negative means first becomes last, second becomes first, etc. turning right


with open('2020 input') as file:
    directions = [line.strip() for line in file]
x, y, = 0, 0
for dir in directions:
    action, value = dir[0], int(dir[1:])

    if action == 'F':
        if compass[0] == 'N':
            y += value
        elif compass[0] == 'S':
            y -= value
        elif compass[0] == 'E':
            x += value
        elif compass[0] == 'W':
            x -= value

    elif action == 'L':
        compass.rotate(value//90)
    elif action == 'R':
        compass.rotate(-1 * value//90)

    elif action == 'N':
        y += value
    elif action == 'S':
        y -= value
    elif action == 'E':
        x += value
    elif action == 'W':
        x -= value

print(f"Part 1: {abs(y) + abs(x)}")