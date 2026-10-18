visited = set()

with open("2015 input") as file:
    directions = file.readlines()[0]


x,y = 0, 0
visited.add((x, y))
for direction in directions:
    if direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "^":
        y += 1
    else :
        y -= 1

    visited.add((x,y))

print(f"Part 1: {len(visited)}")


santa_x, santa_y, robosanta_x, robosanta_y = 0, 0, 0, 0
visited = {(santa_x, santa_y)}

for i, direction in enumerate(directions):
    if i % 2 == 0: #santa
        if direction == "<":
            santa_x -= 1
        elif direction == ">":
            santa_x += 1
        elif direction == "^":
            santa_y += 1
        else:
            santa_y -= 1

    else: #robosanta
        if direction == "<":
            robosanta_x -= 1
        elif direction == ">":
            robosanta_x += 1
        elif direction == "^":
            robosanta_y += 1
        else:
            robosanta_y -= 1

    visited.add((santa_x, santa_y))
    visited.add((robosanta_x, robosanta_y))

print(f"Part 2: {len(visited)}")

