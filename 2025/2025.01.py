from collections import deque

with open('2025 input') as file:
    lines = [line.strip() for line in file]

dial = deque(list(range(100)))
dial.rotate(50)
print(dial)
#positive is left, negative is right

c = 0
c2 = 0

for line in lines:
    print(line)
    dir, mag = line[0], int(line[1:])
    if dir == 'L':
        for _ in range(mag):
            dial.rotate(-1)
            if dial[0] == 0:
                c2 += 1
    else:
        for _ in range(mag):
            dial.rotate(1)
            if dial[0] == 0:
                c2 += 1
    print(dial)
    if dial[0] == 0:
        c += 1

print(f"Part 1: {c}")
print(f"Part 2: {c2}")
