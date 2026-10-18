from collections import defaultdict, Counter

with open('2016 input') as file:
    message = [line.strip() for line in file]

d = defaultdict(list)

for line in message:
    for i, char in enumerate(line):
        d[i].append(char)


correct_message_part1 = ""
correct_message_part2 = ""
for i in d.values():
    c = Counter(i)
    m = max(c.values())
    ml = min(c.values())
    for j in c.keys():
        if c[j] == m:
            correct_message_part1 += j
        elif c[j] == ml:
            correct_message_part2 += j

print(f"Part 1: {correct_message_part1}")
print(f"Part 2: {correct_message_part2}")