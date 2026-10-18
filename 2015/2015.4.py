import hashlib

key = "ckczppom"
i = 0
found5 = False

while True:
    string = key + str(i)
    hash = hashlib.md5(string.encode()).hexdigest()[:6]
    if hash[:5] == '00000' and not found5:
        found5 = True
        print(f"Part 1: {i}")

    if hash == '000000':
        print(f"Part 2: {i}")
        break
    i += 1




