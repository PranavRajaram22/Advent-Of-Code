from collections import defaultdict


registers = defaultdict(int)

with open('2017 input.txt') as file:
    lines = [line.strip().split(" ") for line in file]


maxes = []
for line in lines:
    statement = line[4:]
    operation = line[:3]
    statement.insert(0, "registers[")
    statement.insert(2, ']')
    statement.insert(1, '\'')

    statement.insert(3, '\'')
    statement = ''.join(statement)
    if eval(statement):
        if operation[1] == 'inc':
            registers[operation[0]] += int(operation[2])
        elif operation[1] == 'dec':
            registers[operation[0]] -= int(operation[2])

    maxes.append(max(registers.values()))


print(f'Part 1: {max(registers.values())}')
print(f"Part 2: {max(maxes)}")


