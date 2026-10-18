from copy import copy

with open("2017 input.txt") as file:
    banks = file.readline()

banks = banks.split("\t")
banks = list(map(int, banks))

part1 = 0
visited = [copy(banks)]

while True:
    maximum = max(banks)
    bank = banks.index(maximum)
    banks[bank] = 0

    index = (bank+1)%len(banks)
    while maximum > 0:
        banks[index] += 1
        maximum -= 1
        index = (index+1) % len(banks)

    part1 += 1
    if banks in visited:
        print(f"Part 1: {part1}")
        part2 = abs(visited.index(banks) - len(visited))
        print(f"Part 2: {part2}")
        break
    else:
        visited.append(copy(banks))


