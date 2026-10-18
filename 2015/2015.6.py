lights = []

#0 is off, 1 is on


for y in range(1000):
    row = []
    for x in range(1000):
        row.append([x, y, 0])

    lights.append(row)


with open('2015 input') as file:
    instructions = [line.strip().split(" ") for line in file]

for instruction in instructions:
    if instruction[0] == 'turn':
        start = list(map(int, instruction[2].split(",")))
        finish = list(map(int, instruction[4].split(",")))
        if instruction[1] == 'on':
            for y in range(start[1], finish[1]+1):
                for x in range(start[0], finish[0]+1):
                    lights[y][x][2] = 1

        elif instruction[1] == 'off':
            for y in range(start[1], finish[1]+1):
                for x in range(start[0], finish[0]+1):
                    lights[y][x][2] = 0

    else:
        start = list(map(int, instruction[1].split(",")))
        finish = list(map(int, instruction[3].split(",")))

        for y in range(start[1], finish[1] + 1):
            for x in range(start[0], finish[0] + 1):
                lights[y][x][2] = 1-lights[y][x][2]

count = 0
for y, row in enumerate(lights):
    for x, light in enumerate(row):
        if light[2] == 1:
            count += 1
            lights[y][x][2] = 0


print(f"Part 1: {count}")

for instruction in instructions:
    if instruction[0] == 'turn':
        start = list(map(int, instruction[2].split(",")))
        finish = list(map(int, instruction[4].split(",")))
        if instruction[1] == 'on':
            for y in range(start[1], finish[1]+1):
                for x in range(start[0], finish[0]+1):
                    lights[y][x][2] += 1

        elif instruction[1] == 'off':
            for y in range(start[1], finish[1]+1):
                for x in range(start[0], finish[0]+1):
                    lights[y][x][2] = max(lights[y][x][2]-1, 0)

    else:
        start = list(map(int, instruction[1].split(",")))
        finish = list(map(int, instruction[3].split(",")))

        for y in range(start[1], finish[1] + 1):
            for x in range(start[0], finish[0] + 1):
                lights[y][x][2] += 2



brightness = 0
for y, row in enumerate(lights):
    for x, light in enumerate(row):
        if light[2] > 0:
            brightness += light[2]


print(f"Part 2: {brightness}")
