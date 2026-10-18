num = "1113122113"

def look_and_say(num):
    groups = []
    currgroup = [num[0]]

    for i in range(1, len(num)):
        if num[i] == currgroup[-1]:
            currgroup.append(num[i])
        else:
            groups.append(currgroup)
            currgroup = [num[i]]
    groups.append(currgroup)

    newnum = ""
    for group in groups:
        newnum += "" + str(len(group)) + str(group[0])
    return newnum

for i in range(40):
    num = look_and_say(num)


print(f"Part 1: {len(num)}")

for i in range(10):
    num = look_and_say(num)

print(f"Part 2: {len(num)}")