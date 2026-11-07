from itertools import zip_longest

with open('2021 input') as file:
    nums = [line.strip() for line in file]


change = list(zip_longest(*nums))

maxnum, minnum = "", ""

for i in change:
    if i.count("1") > i.count('0'):
        maxnum += "1"
        minnum += '0'
    else:
        maxnum += "0"
        minnum += '1'


maxnum, minnum = int(maxnum, 2), int(minnum, 2)

print(f"Part 1: {maxnum*minnum}")

oxygen = nums.copy()
co2 = nums.copy()


i = 0

while True:
    col = list(zip_longest(*oxygen))[i]
    if col.count("0") > col.count("1"):
        numidx = 0
        while numidx < len(oxygen):
            if oxygen[numidx][i] != '0':
                oxygen.remove(oxygen[numidx])
            else:
                numidx += 1

    else:
        numidx = 0
        while numidx < len(oxygen):
            if oxygen[numidx][i] != '1':
                oxygen.remove(oxygen[numidx])
            else:
                numidx += 1
    i += 1
    if len(oxygen) == 1:
        break


i = 0

while True:
    col = list(zip_longest(*co2))[i]
    if col.count("0") <= col.count("1"):
        numidx = 0
        while numidx < len(co2):
            if co2[numidx][i] != '0':
                co2.remove(co2[numidx])
            else:
                numidx += 1

    else:
        numidx = 0
        while numidx < len(co2):
            if co2[numidx][i] != '1':
                co2.remove(co2[numidx])
            else:
                numidx += 1
    i += 1
    if len(co2) == 1:
        break

a, b = int(oxygen[0], 2), int(co2[0], 2)
print(f"Part 2: {a*b}")