from collections import deque

screen = []

for i in range(6):
    row = deque()
    for j in range(50):
        row.append(".")
    screen.append(row)


with open('2016 input') as file:
    lines = [line.strip() for line in file]

for line in lines:

    line = line.split(" ")
    if line[0] == 'rect':
        A, B = list(map(int, line[1].split('x')))
        for yi in range(B):
            for xi in range(A):
                screen[yi][xi] = '#'
    elif line[0] == 'rotate':
        if line[1] == 'row':
            row = int(line[2].split("=")[1])
            mag = int(line[-1])
            screen[row].rotate(mag)

        elif line[1] == 'column':
            col = int(line[2].split("=")[1])
            mag = int(line[-1])

            column = deque()
            for yi in range(len(screen)):
                column.append(screen[yi][col])

            column.rotate(mag)

            for yi in range(len(screen)):
                screen[yi][col] = column[yi]



c = 0
for row in screen:
    c += row.count("#")

print(f"Part 1: {c}")

print(f"Part 2:")
for row in screen:
    print(row)