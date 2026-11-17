with open('2022 input') as file:
    lines = [line.strip() for line in file]


groups = []

currgroup = []

for line in lines:
    if line == '':
        groups.append(currgroup.copy())
        currgroup = []
    else:
        currgroup.append(line)

groups.append(currgroup.copy())

for i, group in enumerate(groups):
    groups[i] = sum(list(map(int, group)))


print(f'Part 1: {max(groups)}')

groups.sort(reverse=True)

print(f"Part 2: {groups[0] + groups[1] + groups[2]}")