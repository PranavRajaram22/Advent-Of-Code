import re

pattern = re.compile(r'mul\((\d+),(\d+)\)')

with open('2024 input') as file:
    memory = [line.strip() for line in file]

c = 0

for line in memory:
    muls = list(re.findall(pattern, line))

    for m in muls:
        c += int(m[0]) * int(m[1])

print(f"Part 1: {c}")

p2 = re.compile(r'do\(\)')
p3 = re.compile(r'don\'t\(\)')

c = 0
enabled = True
for line in memory:
    for i in range(len(line)):
        m = re.match(pattern, line[i:])
        if m and enabled:
            c += int(m.group(1)) * int(m.group(2))

        m = re.match(p2, line[i:])
        if m:
            enabled = True

        m = re.match(p3, line[i:])
        if m:
            enabled = False

print(f"Part 2: {c}")