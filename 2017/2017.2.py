with open('2017 input.txt') as file:
    spreadsheet = [line.strip() for line in file]

checksum_part1 = 0
checksum_part2 = 0

for line in spreadsheet:
    line = line.replace("\t", " ")
    line = line.split(" ")
    line = list(map(int, line))
    checksum_part1 += max(line) - min(line)

    for i in range(len(line)):
        for j in range(len(line)):
            if line[i]%line[j] == 0 and i != j:
                checksum_part2 += line[i]//line[j]

print(f"Part 1: {checksum_part1}")
print(f"Part 2: {checksum_part2}")
