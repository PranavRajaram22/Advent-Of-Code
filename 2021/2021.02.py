with open('2021 input') as file:
    lines = [line.strip() for line in file]

d, h = 0, 0

for line in lines:
    line = line.split(" ")

    dir, mag = line
    mag = int(mag)

    if dir == 'forward':
        h += mag
    elif dir == 'down':
        d += mag
    else:
        d -= mag


print(f"Part 1: {d*h}")

d, h, aim = 0, 0, 0

for line in lines:
    line = line.split(" ")

    dir, mag = line
    mag = int(mag)

    if dir == 'forward':
        h += mag
        d += aim*mag
    elif dir == 'down':
        aim += mag
    else:
        aim -= mag

print(f"Part 2: {d*h}")

