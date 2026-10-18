keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

code = 0

with open('2016 input') as file:
    instructions = [line.strip() for line in file]


x, y = 1, 1
for line in instructions:
    for i in line:
        if i == 'L':
            x = max(0, x-1)
        elif i == 'R':
            x = min(2, x+1)
        elif i == 'D':
            y = min(2, y+1)
        elif i == 'U':
            y = max(0, y-1)
    code = code*10 + keypad[y][x]

print(f"Part 1: {code}")


code = ""

x, y = 0, 2

keypad = [[None, None, "1", None, None],
          [None, "2", "3", "4", None, None],
          ["5", "6", "7", "8", "9"],
          [None, 'A', 'B', 'C', None],
          [None, None, 'D', None, None]]


for line in instructions:
    for i in line:
        if i == 'L' and 0 <= x-1 <= 4 and keypad[y][x-1]:
            x = max(0, x-1)
        elif i == 'R' and 0 <= x+1 <= 4 and keypad[y][x+1]:
            x = min(4, x+1)
        elif i == 'D' and 0 <= y+1 <= 4 and keypad[y+1][x]:
            y = min(4, y+1)
        elif i == 'U' and 0 <= y-1 <= 4 and keypad[y-1][x]:
            y = max(0, y-1)

    code += keypad[y][x]

print(f"Part 2: {code}")