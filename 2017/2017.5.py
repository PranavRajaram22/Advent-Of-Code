with open('2017 input.txt') as file:
    offsets = [int(line.strip()) for line in file]


i = 0
part1 = 0
while i in range(0, len(offsets)):
    jump = offsets[i]
    offsets[i] += 1
    i += jump
    part1 += 1

print(f"Part 1: {part1}")
