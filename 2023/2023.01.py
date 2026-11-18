with open('2023 input') as file:
    lines = [line.strip() for line in file]


total = 0
for line in lines:
    c = 0
    for i in line:
        try:
            i = int(i)
            c += i*10
            break
        except ValueError:
            continue

    for z in range(len(line)-1, -1, -1):
        i = line[z]
        try:
            i = int(i)
            c += i
            break
        except ValueError:
            continue
    total += c

print(f"Part 1: {total}")

minsize = 3
maxsize = 5

nums = {'one':1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
        "eno":1, "owt":2, "eerth":3, "rouf":4, "evif":5, 'xis':6, "neves":7, "thgie":8, 'enin':9}
total = 0
for line in lines:
    newline = ""
    for i in range(len(line)):
        try:
            newline += str(int(line[i]))
        except ValueError:
            pass
        found = False
        for k in range(minsize, maxsize+1):
            if line[i:i+k] in nums.keys():
                newline += str(nums[line[i:i+k]])
                break


    c = int(newline[0]) * 10 + int(newline[-1])
    total += c

print(f"Part 2: {total}")
