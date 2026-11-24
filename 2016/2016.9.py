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

i = 0
c = 0
def rec(substring, reps):
    total = 0
    i = 0
    while i < len(substring):
        m = re.match(pattern, substring[i:])
        if m:
            total += reps*rec(substring[i+len(m.group(0)): i+len(m.group(0)) + int(m.group(1))], int(m.group(2)))
            i += len(m.group(0)) + int(m.group(1))
        else:
            total += reps
            i += 1

    return total

while i < len(string):
    m = re.match(pattern, string[i:])
    if m:
        m0 = m.group(0)
        m1 = m.group(1)
        m2 = m.group(2)
        substring = string[i+len(m0): i+len(m0) + int(m1)]
        c += rec(substring, int(m2))
        i += int(m1)+len(m.group(0))
    else:
        c += 1
        i += 1

print(c)
#XABCABCABCABCABCABCY -> 20
