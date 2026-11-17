# "1" uses 2
# "4" uses 4
# "7" uses 3
# "8" uses 7


with open('2021 input') as file:
    lines = [line.strip() for line in file]

total = 0
for line in lines:
    line = line.split(" ")

    i = line.index("|")+1

    while i < len(line):
        s = len(line[i])
        if s in [2, 4, 3, 7]:
            total += 1
        i += 1

print(f"Part 1: {total}")

for line in lines:
    input, output = line.split(" | ")
    input, output = input.split(" "), output.split(" ")
    print(input, output)