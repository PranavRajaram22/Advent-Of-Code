with open('2018 input') as file:
    nums = [line.strip() for line in file]

equation = "0"

for num in nums:
    equation += num

print(f"Part 1: {eval(equation)}")

s = 0

seen = set()

i = 0
while True:
    for num in nums:
        s += int(num)
        if s in seen:
            print(f"Part 2: {s}")
            exit()
        else:
            seen.add(s)


