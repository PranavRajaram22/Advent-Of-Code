with open('2019 input') as file:
    masses = [int(line.strip()) for line in file]

fuel = 0

for mass in masses:
    fuel += mass//3-2

print(f"Part 1: {fuel}")

fuel = 0
for mass in masses:
    mass = mass//3 - 2
    while mass >= 0:
        fuel += mass
        mass = mass//3-2

print(f"Part 2: {fuel}")