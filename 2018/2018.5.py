with open('2018 input') as file:
    polymer = file.readline()

i = 0
newpolymer = ""
destroyed = False
while not destroyed:
    i = 0
    while i < len(polymer):
        if len(polymer[i:i+2]) == 2 and abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
            i += 2
            destroyed = True

        else:
            newpolymer += polymer[i]
            i += 1

    polymer = newpolymer
    newpolymer = ""
    if not destroyed:
        break
    destroyed = False
print(f"Part 1: {len(polymer)}")