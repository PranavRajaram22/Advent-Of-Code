inp = "254032-789860"

def adj(num):
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return True

    return False

def inc(num):
    for i in range(len(num)-1):
        if num[i+1] < num [i]:
            return False

    return True

def isValid(num):
    return adj(num) and inc(num)


count = 0

min, max = list(map(int, inp.split("-")))


for num in range(min, max+1):
    if isValid(str(num)):
        count += 1

print(f"Part 1: {count}")

def adj2(num):
    sets = []
    currset = [num[0]]
    for dig in num[1:]:
        if dig == currset[0]:
            currset.append(dig)
        else:
            sets.append(currset.copy())
            currset = [dig]

    sets.append(currset.copy())
    return any(len(i) == 2 for i in sets)


for num in range(min, max+1):
    if isValid(str(num)):
        count += 1



def isValid2(num):
    return inc(num) and adj2(num)

count = 0
for num in range(min, max+1):
    if isValid2(str(num)):
        count += 1

print(f"Part 2: {count}")
