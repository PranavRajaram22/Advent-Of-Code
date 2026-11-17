with open('2022 input') as file:
    lines = [line.strip().split(",") for line in file]

c1 = 0
c2 = 0
for line in lines:
    line[0] = list(map(int, line[0].split("-")))
    line[1] = list(map(int, line[1].split('-')))
    line = [*line[0], *line[1]]


    x1, y1, x2, y2 = line

    if (y2 >= y1 and x2 <= x1) or (y2 <= y1 and x2 >= x1):
        print(line)
        c1 += 1
        c2 += 1

    elif (y2 >= y1 >= x2 >= x1) or (y1 >= y2 >= x1 >= x2):
        print(line)
        c2 += 1

print(f'Part 1: {c1}')
print(f'Part 2: {c2}')


#x1, y1, x2, y2

#x1, x2, y1, y2


