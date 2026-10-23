import math
from collections import defaultdict, Counter


def manhattan_distance(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1] - coord2[1])

with open('2019 input') as file:
    instructions = [line.strip() for line in file]

for i, inst in enumerate(instructions):
    instructions[i] = tuple(inst.split(","))

visited = defaultdict(set)

for instruction in instructions:
    x, y = 0,0
    for direction in instruction:
        dir, mag = direction[0], int(direction[1:])
        if dir == 'R':
            for dx in range(1, mag+1):
                x += 1
                visited[instruction].add((x, y))
        elif dir == 'L':
            for dx in range(1, mag+1):
                x -= 1
                visited[instruction].add((x, y))

        if dir == 'U':
            for dy in range(1, mag+1):
                y += 1
                visited[instruction].add((x, y))


        elif dir == 'D':
            for dy in range(1, mag+1):
                y -= 1
                visited[instruction].add((x, y))



minManDist = math.inf

print("Done making visited")
visited = [*i for i in visited.values()]
print("Done unpacking")

dupes = set()

coord_Counter = Counter(visited)
for coord in coord_Counter:
    if coord_Counter[coord] >= 2:
        dupes.add(coord)


for dupe in dupes:
    minManDist = min(minManDist, manhattan_distance(dupe, (0,0)))

print(f"Part 1: {minManDist}")