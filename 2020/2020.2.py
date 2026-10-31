with open('2020 input') as file:
    passwords = [line.strip() for line in file]

for i, line in enumerate(passwords):

    line = line.split(" ")
    line[1] = line[1][:-1]

    line[0] = list(map(int, line[0].split("-")))

    passwords[i] = line


def isValid(range, letter, password):
    mincount, maxcount = range

    count = password.count(letter)

    return mincount <= count <= maxcount

part1count = 0

for password in passwords:
    if isValid(*password):
        part1count += 1

print(f"Part 1: {part1count}")

def isValid2(pos, letter, password):
    return (password[pos[0]-1] == letter) ^ (password[pos[1]-1] == letter)

part2count = 0

for password in passwords:
    if isValid2(*password):
        part2count += 1

print(f"Part 2: {part2count}")

