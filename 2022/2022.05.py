from collections import defaultdict, deque

with open('2022 input') as file:
    lines = [line.replace("\n", "") for line in file]

stacks = defaultdict(deque)
b = lines.index("")-1
for y, line in enumerate(lines):
    if y < b:
        for i, l in enumerate(line):
            if i%4 == 1 and l != ' ':
                stacks[i//4 + 1].append(l)


#[top, ....., bottom]

for line in lines[b+2:]:
    line = line.split(" ")
    mag, fro, to = int(line[1]), int(line[3]), int(line[5])
    for _ in range(mag):
        stacks[to].appendleft(stacks[fro].popleft())


code = ""

for i in range(1, max(stacks.keys())+1):
    code += stacks[i][0]

print(f"Part 1: {code}")
stacks = defaultdict(list)
with open('2022 input') as file:
    lines = [line.replace("\n", "") for line in file]

stacks = defaultdict(list)
b = lines.index("")-1
for y, line in enumerate(lines):
    if y < b:
        for i, l in enumerate(line):
            if i%4 == 1 and l != ' ':
                stacks[i//4 + 1].append(l)


for line in lines[b+2:]:
    line = line.split(" ")
    mag, fro, to = int(line[1]), int(line[3]), int(line[5])

    for i in range(mag-1, -1, -1):
        stacks[to].insert(0, stacks[fro].pop(i))

code = ""

for i in range(1, max(stacks.keys())+1):
    code += stacks[i][0]

print(f"Part 2: {code}")