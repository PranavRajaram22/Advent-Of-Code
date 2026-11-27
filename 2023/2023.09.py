with open('2023 input') as file:
    lines = [list(map(int, line.strip().split(" "))) for line in file]

def goDown(sequence):
    newsequence = []
    for i in range(len(sequence)-1):
        newsequence.append(sequence[i+1]-sequence[i])

    return newsequence


def calcTerm(sequence):
    allsequences = [sequence]

    while not all(i == 0 for i in sequence):
        sequence = goDown(sequence)
        allsequences.append(sequence)

    allsequences.reverse()
    for i in range(1, len(allsequences)):
        allsequences[i].append(allsequences[i][-1] + allsequences[i-1][-1])

    return allsequences[-1][-1]

c = 0
for line in lines:
    c += calcTerm(line)

print(f"Part 1: {c}")

def calcTerm2(sequence):
    allsequences = [sequence]

    while not all(i == 0 for i in sequence):
        sequence = goDown(sequence)
        allsequences.append(sequence)

    allsequences.reverse()
    for i in range(1, len(allsequences)):
        allsequences[i].insert(0, allsequences[i][0]-allsequences[i-1][0])

    return allsequences[-1][0]



c = 0
for line in lines:
    c += calcTerm2(line)

print(f"Part 2: {c}")