with open('2017 input.txt') as file:
    passphrases = [line.strip() for line in file]

part1 = 0
part2 = 0
for phrase in passphrases:
    phrase = phrase.split(" ")
    if not any(phrase.count(word) >= 2 for word in phrase):
        part1 += 1

    for i, word in enumerate(phrase):
        phrase[i] = sorted(word)

    if not any(phrase.count(word) >= 2 for word in phrase):
        part2 += 1


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


