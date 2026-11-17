with open('2021 input') as file:
    lines = [line.strip() for line in file]

total = 0
totalpart2 = []
scores = {")":3, "]":57, "}":1197, ">":25137}
scorespart2 = {"(":1, "[":2, "{":3, "<":4}
for line in lines:
    stack = []
    t = 0
    isBad = False
    for i in line:
        if i in ["(", "[", "{", "<"]:
            stack.append(i)
        else:
            if (i == ')' and stack[-1] != '(') or (i == ']' and stack[-1] != '[') or (i == '}' and stack[-1] != "{") or (i == ">" and stack[-1] != "<"): #invalid:
                total += scores[i]
                isBad = True
                break
            else:
                stack.pop(-1)


    if not isBad:
        stack.reverse()
        for k in stack:
            t *= 5
            t += scorespart2[k]
        totalpart2.append(t)


print(f"Part 1: {total}")

totalpart2.sort()
print(f'Part 2: {totalpart2[len(totalpart2)//2]}')