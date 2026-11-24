import math
from collections import defaultdict
from copy import copy
from itertools import combinations
from more_itertools import flatten

with open('2025 input') as file:
    lines = [tuple(map(int, line.strip().split(","))) for line in file]


def dist(p1, p2):
    x1, y1, z1, x2, y2, z2 = *p1, *p2
    z = z2-z1
    y = y2-y1
    x = x2-x1
    return math.sqrt(x**2 + y**2 + z**2)

combs = list(combinations(lines, 2))
combs = sorted(combs, key=lambda i: dist(*i))
first_empty_circuit = 0
circuits = defaultdict(list)


c = 0
i = 0
importantpair = []
found = False
while c < 1000:
    pair = combs[i]
    allcircuitsmerged = list(flatten(circuits.values()))
    if pair[0] in allcircuitsmerged and pair[1] in allcircuitsmerged: #both already part of a circuit
        for n, circuit in enumerate(circuits.values()):
            if pair[0] in circuit and pair[1] in circuit: #both part of the same circuit; just increase connection count
                c += 1
                break
            elif pair[0] in circuit: #pair is in separate but already existing circuits; merge circuits
                for num, circuit2 in enumerate(circuits.values()):
                    if pair[1] in circuit2:
                        circuit_to_merge = circuit2.copy()
                        circuits[num] = []
                        circuits[n] = circuits[n] + circuit_to_merge
                        c += 1
                        break

    else: #at least one box is not a part of an existing circuit
        if pair[0] in allcircuitsmerged: #need to add pair[1] to pair[0]'s circuit
            for num, circuit in circuits.items():
                if pair[0] in circuit:
                    circuits[num].append(pair[1])
                    c += 1
                    break

        elif pair[1] in allcircuitsmerged: #need to add pair[0] to pair[1]'s circuit
            for num, circuit, in circuits.items():
                if pair[1] in circuit:
                    circuits[num].append(pair[0])
                    c += 1
                    break

        else: #neither box is a part of a circuit; add to new circuit
            circuits[first_empty_circuit].append(pair[0])
            circuits[first_empty_circuit].append(pair[1])
            c += 1
            while circuits[first_empty_circuit] != []:
                first_empty_circuit += 1

    i += 1

sizes = []
for m in circuits.values():
    sizes.append(len(m))

sizes.sort(reverse=True)
print(f'Part 1: {sizes[0]*sizes[1]*sizes[2]}')

while True:
    pair = combs[i]
    allcircuitsmerged = list(flatten(circuits.values()))
    if pair[0] in allcircuitsmerged and pair[1] in allcircuitsmerged:  # both already part of a circuit
        for n, circuit in enumerate(circuits.values()):
            if pair[0] in circuit and pair[
                1] in circuit:  # both part of the same circuit; just increase connection count
                c += 1
                break
            elif pair[0] in circuit:  # pair is in separate but already existing circuits; merge circuits
                for num, circuit2 in enumerate(circuits.values()):
                    if pair[1] in circuit2:
                        circuit_to_merge = circuit2.copy()
                        circuits[num] = []
                        circuits[n] = circuits[n] + circuit_to_merge
                        c += 1
                        break

    else:  # at least one box is not a part of an existing circuit
        if pair[0] in allcircuitsmerged:  # need to add pair[1] to pair[0]'s circuit
            for num, circuit in circuits.items():
                if pair[0] in circuit:
                    circuits[num].append(pair[1])
                    c += 1
                    break

        elif pair[1] in allcircuitsmerged:  # need to add pair[0] to pair[1]'s circuit
            for num, circuit, in circuits.items():
                if pair[1] in circuit:
                    circuits[num].append(pair[0])
                    c += 1
                    break

        else:  # neither box is a part of a circuit; add to new circuit
            circuits[first_empty_circuit].append(pair[0])
            circuits[first_empty_circuit].append(pair[1])
            c += 1
            while circuits[first_empty_circuit] != []:
                first_empty_circuit += 1

    i += 1
    for num, circuit in circuits.items():
        if len(circuit) == len(lines) and not found:
            importantpair = copy(pair)
            print(f'Part 2: {importantpair[0][0] * importantpair[1][0]}')
            exit()



