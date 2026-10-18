from itertools import permutations, pairwise

with open('2015 input') as file:
    lines = [line.strip() for line in file]

for i, line in enumerate(lines):
    line = line.split(" ")
    line.pop(1)
    line.pop(3)
    line.pop(3)
    line.pop(3)
    line.pop(3)
    line.pop(3)
    line.pop(3)
    line[2] = int(line[2])
    state = line.pop(1)
    if state == 'lose':
        line[1] *= -1
    line[-1] = line[-1][:-1]
    lines[i] = line


firstPerson = lines[0][0]
ppl = [firstPerson]

for line in lines:
    if line[0] == firstPerson:
        ppl.append(line[2])

perms = list(permutations(ppl))

totalhappiness = []

for perm in perms:
    first = perm[0]
    last = perm[-1]
    pairs = list(pairwise(perm))
    pairs.append((first, last))
    happiness = 0
    for pair in pairs:
        for line in lines:
            if pair[0] in line and pair[1] in line:
                happiness += line[1]

    totalhappiness.append(happiness)


print(f"Part 1: {max(totalhappiness)}")

for person in ppl:
    lines.append([person, 0, 'you'])

ppl.append("you")

perms = list(permutations(ppl))

totalhappiness = []


for perm in perms:
    first = perm[0]
    last = perm[-1]
    pairs = list(pairwise(perm))

    pairs.append((first, last))
    happiness = 0
    for pair in pairs:
        for line in lines:
            if pair[0] in line and pair[1] in line:
                happiness += line[1]

    totalhappiness.append(happiness)
print(f"Part 2: {max(totalhappiness)}" )


