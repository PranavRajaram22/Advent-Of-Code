from itertools import combinations as comb, permutations as perm

with open('2024 input') as file:
    lines = [line.strip() for line in file]

rules = []
updates = []

isRules = True
for line in lines:
    if line == '':
        isRules = False
    elif isRules:
        rules.append(list(map(int, line.split('|'))))
    else:
        updates.append(list(map(int, line.split(","))))

def isValid(update):
    combs = list(comb(update, 2))

    for c in combs:
        if [c[1], c[0]] in rules:
            return False

    return True

total = 0
total2 = 0
for x, update in enumerate(updates):
    if isValid(update):
        total += update[len(update)//2]
    else:
        valid = False
        while not valid:
            for i in range(len(update)):
                for j in range(i+1, len(update)):
                    if [update[j], update[i]] in rules:
                        update[i], update[j] = update[j], update[i]
                        if isValid(update):
                            valid = True
                            break
                if valid:
                    break

        total2 += update[len(update)//2]


print(f'Part 1: {total}')
print(f'Part 2: {total2}')



