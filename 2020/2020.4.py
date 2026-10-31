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
part2count = 0
for i, passport in enumerate(passports):
    newpassport = dict()
    newpassportcategories = []
    for line in passport:
        line = line.split(' ')
        for characteristic in line:
            category, value = characteristic.split(":")
            newpassport[category] =  value
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
part1validpassports = []

for passport in passports:

    categories = passport[1]
    if all(cat in categories for cat in required_categories):
        part1count += 1
        part1validpassports.append(passport[0])

print(f"Part 1: {part1count}")
for passport in part1validpassports:
    isValid = True
    year = int(passport['byr'])
    if not 1920 <= year <= 2020:
        isValid = False

    year = int(passport['iyr'])
    if not 2010 <= year <= 2020:
        isValid = False

    year = int(passport['eyr'])
    if not 2020 <= year <= 2030:
        isValid = False

    height = passport['hgt']
    if len(height) > 2:
        mag, unit = int(height[:-2]), height[-2:]
        if unit == 'cm':
            if not 150 <= mag <= 193:
                isValid = False
        elif unit == 'in':
            if not 59 <= mag <= 76:
                isValid = False

        else:
            isValid = False
    else:
        isValid = False

    hx = passport['hcl']
    if not hx.startswith("#"):
        isValid = False

    else:
        validchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if len(hx) != 7 or any(i not in validchars for i in hx[1:]):
            isValid = False


    eyecol = passport['ecl']

    allowed_eyecol = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if eyecol not in allowed_eyecol:
        isValid = False

    countryid = passport['pid']

    if len(countryid) == 9:
        try:
            id = int(countryid)
        except TypeError:
            isValid = False

    else:
        isValid = False


    if isValid:
        part2count += 1


print(f"Part 2: {part2count}")

