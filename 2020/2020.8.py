from copy import copy

with open('2020 input') as file:
    masterprogram = [line.strip() for line in file]


visited = set()

def run(program):
    i = 0

    acc = 0
    while True:
        inst, mag = program[i].split(" ")
        if inst == 'acc':
            acc += int(mag)
            i += 1
        elif inst == 'nop':
            i += 1

        elif inst == 'jmp':
            i += int(mag)

        if i in visited:
            return acc
        else:
            visited.add(i)

print(f"Part 1: {run(masterprogram.copy())}")

nops = []
jmps = []

for i, line in enumerate(masterprogram):
    if line.startswith("jmp"):
        jmps.append(i)

    elif line.startswith("nop"):
        nops.append(i)


def run2(program):
    i = 0
    acc = 0
    visited = set()
    while i < len(program):
        inst, mag = program[i].split(" ")
        if inst == 'acc':
            acc += int(mag)
            i += 1
        elif inst == 'nop':
            i += 1

        elif inst == 'jmp':
            i += int(mag)

        if i in visited:
            return None
        else:
            visited.add(i)

    return acc

for nop in nops:
    program = masterprogram.copy()
    line = program[nop]
    line = line.split(" ")
    line[0] = 'jmp'
    program[nop] = " ".join(line)

    p = run2(program)
    if p:
        print(f"Part 2: {p}")
        exit()

for jmp in jmps:
    program = masterprogram.copy()
    line = program[jmp]
    line = line.split(" ")
    line[0] = 'nop'
    program[jmp] = " ".join(line)

    p = run2(program)
    if p:
        print(f"Part 2: {p}")
        exit()




