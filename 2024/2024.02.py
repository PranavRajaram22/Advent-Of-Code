def safe(line):
    if (sorted(line) == line or sorted(line, reverse=True) == line):
        for i in range(len(line)-1):
            if not (1 <= abs(line[i] - line[i+1]) <= 3):
                return False

        return True

    return False

def safe2(line):
    if safe(line):
        return True

    for i in range(len(line)):
        l = line.copy()
        l.pop(i)
        if safe(l):
            return True

    return False


with open('2024 input') as file:
    lines = [list(map(int, line.strip().split(" "))) for line in file]

c = 0
c2 = 0
for line in lines:
    if safe(line):
        c += 1
    if safe2(line):
        c2 += 1

print(f"Part 1: {c}")
print(f"Part 2: {c2}")