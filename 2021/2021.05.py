from collections import defaultdict

with open('2021 input') as file:
    lines = [line.strip() for line in file]


coords = defaultdict(int)

for line in lines:
    line = line.split("->")

    for i, x in enumerate(line):
        line[i] = list(map(int, x.split(',')))
    print(line)
    x1, y1, x2, y2 = [*i for i in line]
    print(x1, y1, x2, y2)

    if x1 == x2: #horizontal
        for y in range(y1, y2+1):
            coords[(x1, y)]+= 1

    elif y1 == y2: #verticall
        for x in range(x1, x2+1):
            coords[(x, y1)] += 1

total = 0

for k, v in coords.items():
    if v > 1:
        print(k)
        total += 1

print(total)