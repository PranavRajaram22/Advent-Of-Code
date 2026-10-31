with open('2020 input') as file:
    lines = [line.strip() for line in file]

passports = []

currpassport = []

for line in lines:
    if line != '' :
        currpassport.append(line)

    else:
        passports.append(currpassport)
        currpassport = []

passports.append(currpassport)
for i, passport in enumerate(passports):
    newpassport = []
    newpassportcategories = []
    for line in passport:
        line = line.split(' ')
        for characteristic in line:
            category, value = characteristic.split(":")
            newpassport.append({category: value})
            newpassportcategories.append(category)

    passports[i] = (newpassport, newpassportcategories)

required_categories = ['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid']

part1count = 0
for passport in passports:
    categories = passport[1]
    if all(cat in categories for cat in required_categories):
        part1count += 1
print(f"Part 1: {part1count}")

