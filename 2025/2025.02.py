from itertools import batched

def invalid(num):
    num = str(num)
    num1, num2 = num[:len(num)//2], num[len(num)//2:]
    return num1 == num2

def invalid2(num):
    lens = [i for i in range(1, len(str(num))) if len(str(num))%i == 0]
    for i in lens:
        batch = batched(str(num), i)
        if len(set(batch)) == 1:
            return True

    return False

with open('2025 input') as file:
    ranges = [line.strip() for line in file][0]

ranges = ranges.split(",")
ranges = [list(map(int, i.split("-"))) for i in ranges]

c = 0
c2 = 0
for r in ranges:
    for i in range(r[0], r[1] + 1):
        if invalid(i):
            c += i
        if invalid2(i):
            c2 += i

print(f"Part 1: {c}")
print(f"Part 2: {c2}")

