from functions_i_use_a_lot import transpose

with open('2023 input') as file:
    lines = [line.strip().split(" ") for line in file]

for i, line in enumerate(lines):
    while '' in line:
        line.remove("")
    line.pop(0)
    lines[i] = list(map(int, line))

races = transpose(lines)
total = 1
for race in races:
    time, rec_dist = race
    c = 0
    for hold_time in range(1, time):
        speed = hold_time
        travel_time = time-hold_time
        dist_traveled = speed*travel_time
        if dist_traveled > rec_dist:
            c += 1
    total *= c

print(f"Part 1: {total}")

with open('2023 input') as file:
    lines = [line.strip().split(" ") for line in file]

for i, line in enumerate(lines):
    while '' in line:
        line.remove("")
    line.pop(0)
    lines[i] = int(''.join(line))


time = lines[0]
rec_dist = lines[1]

c = 0
for hold_time in range(1, time):
    speed = hold_time
    travel_time = time-hold_time
    dist_traveled = speed*travel_time
    if dist_traveled > rec_dist:
        c += 1
total *= c

print(f"Part 2: {c}")


