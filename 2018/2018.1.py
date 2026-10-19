with open('2018 input') as file:
    nums = [line.strip() for line in file]

equation = "0"

for num in nums:
    equation += num

print(f"Part 1: {eval(equation)}")

