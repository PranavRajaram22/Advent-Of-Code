from collections import Counter

with open('2018 input') as file:
    boxes = [line.strip() for line in file]

num_twos = 0
num_threes = 0

for box in boxes:
    count = Counter(box)
    if any(v == 2 for v in count.values()):
        num_twos += 1

    if any(v == 3 for v in count.values()):
        num_threes += 1


print(f"Part 1: {num_twos * num_threes}")

def compare(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1

    return diff == 1

for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        if compare(boxes[i], boxes[j]):
            string = ""
            s1 = boxes[i]
            s2 = boxes[j]
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    string += s1[i]

            print(f"Part 2: {string}")
            exit()
