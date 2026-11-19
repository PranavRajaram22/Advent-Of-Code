from itertools import zip_longest

with open('2024 input') as file:
    lines = [line.strip() for line in file]

for i, line in enumerate(lines):
    line = line.split(" ")
    while "" in line:
        line.remove("")
    lines[i] = list(map(int, line))

lists = list(zip_longest(*lines))

for i, l in enumerate(lists):
    lists[i] = sorted(l)


c = 0

for i in range(len(lists[0])):
    c += abs(lists[0][i] - lists[1][i])

print(f"Part 1: {c}")

c = 0

for i in range(len(lists[0])):
    c += lists[0][i] * lists[1].count(lists[0][i])

print(f"Part 2: {c}")