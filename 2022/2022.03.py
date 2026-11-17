letters = []

for i in range(ord('a'), ord('z')+1):
    letters.append(chr(i))


for i in range(ord('A'), ord('Z')+1):
    letters.append(chr(i))


with open('2022 input') as file:
    lines = [line.strip() for line in file]

total = 0
for line in lines:
    comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
    comp1, comp2 = set(comp1), set(comp2)
    for i in comp1:
        if i in comp2:
            total += letters.index(i) + 1

print(f'Part 1: {total}')

groups = []
currgroup = []

for i, line in enumerate(lines):
    if i%3 == 0 and i != 0:
        groups.append(currgroup.copy())
        currgroup = []
    currgroup.append(set(line))

groups.append(currgroup.copy())

total = 0
for group in groups:
    for i in group[0]:
        if i in group[1] and i in group[2]:
            total += letters.index(i)+1

print(f'Part 2: {total}')