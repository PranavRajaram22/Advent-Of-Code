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

print(stacks)

#[top, ....., bottom]

for line in lines[b+2:]:
    line = line.split(" ")
    mag, fro, to = int(line[1]), int(line[3]), int(line[5])
    print(mag, fro, to)
    for _ in range(mag):
        stacks[to].appendleft(stacks[fro].popleft())

    print(stacks)

code = ""

for i in range(1, max(stacks.keys())+1):
    code += stacks[i][0]

print(code)