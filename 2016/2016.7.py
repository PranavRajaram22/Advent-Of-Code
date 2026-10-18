def isABBA(string):
    for i in range(len(string)-3):
        s = string[i:i+4]
        if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
            return True

    return False

def ABAtoBAB(string):
    babs = []
    for i in range(len(string)-2):
        s = string[i:i+3]
        if s[0] == s[2] and s[0] != s[1]:
            babs.append((s[1] + s[0] + s[1]))

    return babs

part1 = 0
part2 = 0
with open('2016 input') as file:
    addys = [line.strip() for line in file]

for addy in addys:
    nothypernet = []
    hypernet = []

    curr = ""
    inhyp = False
    for char in addy:
        if char == '[':
            nothypernet.append(curr)
            curr = ""
            inhyp = True

        elif char == ']':
            hypernet.append(curr)
            curr = ""
            inhyp = False

        else:
            curr += char
    if inhyp:
        hypernet.append(curr)
    else:
        nothypernet.append(curr)
    if any(isABBA(i) for i in nothypernet) and not any(isABBA(i) for i in hypernet):
        part1 += 1

    for nhyp in nothypernet:

        babs = ABAtoBAB(nhyp)

        if babs and any(j in i for i in hypernet for j in babs):
            part2 += 1




print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


