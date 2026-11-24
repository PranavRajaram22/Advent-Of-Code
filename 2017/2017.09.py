from copy import copy

with open('2017 input.txt') as file:
    lines = [line.strip() for line in file]

total = 0
totalgarbage = 0
for line in lines:
    i = 0
    newstring = ""
    oldstring = line
    while "!" in oldstring:
        while i < len(line):
            if line[i] != '!':
                newstring += line[i]
                i += 1
            else:
                i += 2


        oldstring = copy(newstring)


    isGarbage = False
    newstring = ""

    garbage = 0
    for i in oldstring:
        if i == '<' and not isGarbage:
            isGarbage = True
        elif i == '>' and isGarbage:
            isGarbage = False
        elif not isGarbage:
            newstring += i
        elif isGarbage:
            garbage += 1


    currpos = 0
    c = 0
    for i in newstring:
        if i == '{':
            currpos += 1
        elif i == '}':
            c += currpos
            currpos -= 1

    total += c
    totalgarbage += garbage

print(f"Part 1: {total}")
print(f"Part 2: {totalgarbage}")

