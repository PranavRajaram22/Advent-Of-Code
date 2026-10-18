from copy import copy

with open('2017 input.txt') as file:
    master_offsets = [int(line.strip()) for line in file]


i = 0
part1 = 0

offsets = copy(master_offsets)
while i in range(0, len(offsets)):
    jump = offsets[i]
    offsets[i] += 1
    i += jump
    part1 += 1

print(f"Part 1: {part1}")

offsets = copy(master_offsets)
part2 = 0
i = 0
while i in range(0, len(offsets)):
    jump = offsets[i]
    if offsets[i] < 3:
        offsets[i] += 1
    else:
        offsets[i] -= 1
    i += jump
    part2 += 1

print(f"Part 2: {part2}")