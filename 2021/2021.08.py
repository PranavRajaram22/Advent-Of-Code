# "1" uses 2
# "4" uses 4
# "7" uses 3
# "8" uses 7

# "0" uses 6
# "2" uses 5
# "3" uses 5
# "5" uses 5
# "6" uses 6
# "9" uses 6

with open('2021 input') as file:
    lines = [line.strip() for line in file]

total = 0
for line in lines:
    line = line.split(" ")

    i = line.index("|")+1

    while i < len(line):
        s = len(line[i])
        if s in [2, 4, 3, 7]:
            total += 1
        i += 1

print(f"Part 1: {total}")

total = 0
for line in lines:
    input, output = line.split(" | ")
    input, output = list(map(set, input.split(" "))), list(map(set, output.split(" ")))


    nums = dict()

    for seg in input:
        if len(seg) == 2:
            nums[1] = seg
        elif len(seg) == 3:
            nums[7] = seg
        elif len(seg) == 4:
            nums[4] = seg
        elif len(seg) == 7:
            nums[8] = seg

    for seg in input:
        if len(seg) == 6: #has to be 0, 6, or 9
            seg1 = nums[1]
            seg4 = nums[4]
            if list(set(seg1).difference(set(seg))) and list(set(seg1).difference(set(seg)))[0] in seg1: #its 6
                nums[6] = seg

            else: #either 0 or 9
                if list(set(seg4).difference(set(seg))) and list(set(seg4).difference(set(seg)))[0] in seg4: #its 0
                    nums[0] = seg
                else: #its 9
                    nums[9] = seg

        elif len(seg) == 5: #has to be 2, 3, or 5
            seg1 = nums[1]
            if len(list(set(seg1).difference(set(seg)))) == 0: #its 3
                nums[3] = seg
            else: #its 2 or 5
                seg4 = nums[4]
                if len(list(set(seg4).difference(set(seg)))) == 1: #its 5
                    nums[5] = seg
                else: #its 2
                    nums[2] = seg
    o = ""
    for seg in output:
        for i in range(10):
            if nums[i] == seg:
                o += str(i)
                break

    total += int(o)

print(f"Part 2: {total}")
