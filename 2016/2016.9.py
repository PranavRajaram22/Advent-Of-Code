import re

pattern = re.compile(r'\((\d+)x(\d+)\)')

with open('2016 input') as file:
    string = [line.strip() for line in file][0]

i = 0
c = 0
while i < len(string):
    m = re.match(pattern, string[i:])
    if m:
        a = int(m.group(1))
        b = int(m.group(2))
        i += len(str(a)) + 1 + len(str(b)) + 2 + a
        c += a * b
    else:
        i += 1
        c += 1



print(f"Part 1: {c}")