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