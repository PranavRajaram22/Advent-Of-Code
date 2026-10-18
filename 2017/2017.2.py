with open('2017 input.txt') as file:
    spreadsheet = [line.strip() for line in file]

checksum_part1 = 0

for line in spreadsheet:
    line = line.replace("\t", " ")
    line = line.split(" ")
    line = list(map(int, line))
    checksum_part1 += max(line) - min(line)


print(f"Part 1: {checksum_part1}")
