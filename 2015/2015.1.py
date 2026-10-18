floor = 0

with open('2015 input') as f:
    instructions = f.readlines()[0]


for instruction in instructions:
    if instruction == "(":
        floor += 1
    else:
        floor -= 1

print(f"Part 1: {floor}")

floor = 0

for i, instruction in enumerate(instructions):
    if instruction == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(f"Part 2: {i+1}")
        break