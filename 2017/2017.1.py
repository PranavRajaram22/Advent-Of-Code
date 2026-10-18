with open('2017 input.txt') as file:
    num = file.readline()

num += num[0]

part1 = 0
for i in range(len(num)-1):
    if num[i] == num[i+1]:
        part1 += int(num[i])

print(f"Part 1: {part1}")

num = num[:-1]
jump = len(num)//2
part2 = 0
for i in range(len(num)):
    j = (i + jump)%len(num)
    if num[i] == num[j]:
        part2 += int(num[i])

print(f"Part 2: {part2}")