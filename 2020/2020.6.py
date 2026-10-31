with open('2020 input') as file:
    lines = [line.strip() for line in file]

groups = []

currgroup = []

for line in lines:
    if line != '':
        currgroup.append(line)
    else:
        groups.append(currgroup)
        currgroup = []

groups.append(currgroup)
part1count = 0
for group in groups:
    questions = []
    for person in group:
        for question in person:
            questions.append(question)

    questions = set(questions)
    part1count += len(questions)


print(f"Part 1: {part1count}")

part2count = 0
for group in groups:
    questions = set(group[0])
    for person in group[1:]:
        questions = questions.intersection(set(person))

    part2count += len(questions)

print(f"Part 2: {part2count}")

