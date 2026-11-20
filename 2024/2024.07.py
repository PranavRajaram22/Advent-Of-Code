from collections import deque

with open('2024 input') as file:
    lines = [line.strip() for line in file]



def int_to_base3(n: int):
    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)

    digits = []
    while n > 0:
        n, remainder = divmod(n, 3)
        digits.append(str(remainder))

    base3_str = ''.join(reversed(digits))

    return list(map(int, "-" + base3_str)) if is_negative else list(map(int, base3_str))


def eval(nums, ops):
    c = nums[0]
    i = 1
    j = 0
    while i < len(nums):
        if ops[j] == 0:
            c += nums[i]
        elif ops[j] == 1:
            c *= nums[i]
        else:
            c = int(str(c) + str(nums[i]))
        i += 1
        j += 1

    return c

c = 0
c2 = 0
for x, line in enumerate(lines):
    print(int(x/len(lines)*100))
    goal, nums = line.split(":")
    goal = int(goal)
    nums = list(map(int, nums[1:].split(" ")))
    numops = len(nums)-1
    for i in range(3  **numops):
        x = deque(map(int, list(bin(i)[2:])))
        y = deque(map(int, list(int_to_base3(i))))
        while len(x) < numops:
            x.appendleft(0)
        while len(y) < numops:
            y.appendleft(0)
        if goal == eval(nums, x):
            c += goal
            c2 += goal
            break
        elif goal == eval(nums, y):
            c2 += goal
            break

print(f"Part 1: {c}")
print(f"Part 2: {c2}")


