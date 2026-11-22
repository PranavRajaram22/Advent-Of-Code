import math

from functions_i_use_a_lot import transpose, group_list_by_empty_line

with open('2025 input') as file:
    lines = [line.strip() for line in file]


for i, line in enumerate(lines):
    line = line.split(" ")
    while "" in line:
        line.remove("")
    lines[i] = line


eqs = transpose(lines)
total = 0
for eq in eqs:
    op = eq.pop(-1)
    if op == "+":
        c = 0
        for i in eq:
            c += int(i)
    else:
        c = 1
        for i in eq:
            c *= int(i)

    total += c


print(f"Part 1: {total}")


with open('2025 input') as file:
    lines = [line.replace("\n", '') for line in file]


ops = list(lines.pop(-1))
ops.reverse()


while " " in ops:
    ops.remove(" ")

eqs = transpose(lines)
eqs.reverse()
for i, eq in enumerate(eqs):
    if all(j == ' ' for j in eq):
        eqs[i] = ''

eqs = group_list_by_empty_line(eqs)
for i, eq in enumerate(eqs):
    for j, num in enumerate(eq):
        while None in num:
            num[num.index(None)] = ''

        eqs[i][j] = int("".join(num))


total = 0
for i in range(len(eqs)):
    op = ops[i]
    if op == '+':
        total += sum(eqs[i])
    else:
        total += math.prod(eqs[i])

print(f"Part 2: {total}")

