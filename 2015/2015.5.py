
forbidden_strings = ["ab", 'cd', 'pq', 'xy']

with open('2015 input') as file:
    strings = [line.strip() for line in file]


def isNicePart1(string):
    if string.count('a') + string.count('e') + string.count('i') + string.count("o") + string.count("u") >= 3:
        if not any(i in string for i in forbidden_strings):
            for i in range(0, len(string)-1):
                if string[i] == string[i+1]:
                    return True

    return False


count = 0

for string in strings:
    if isNicePart1(string):
        count += 1

print(f"Part 1: {count}")

count = 0

def isNicePart2(string):
    doubles = []
    triples = []

    for i in range(len(string)-1):
        doubles.append(string[i] + string[i+1])

    for i in range(len(string)-2):
        triples.append(string[i] + string[i+1] + string[i+2])

    if not any(triplet[0] == triplet[2] for triplet in triples):
        return False

    for i in range(len(doubles)):
        for j in range(len(doubles)):
            if doubles[i] == doubles[j] and abs(i-j) > 1:
                return True

    return False

for string in strings:
    if isNicePart2(string):
        count += 1

print(f"Part 2: {count}")


