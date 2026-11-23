from functions_i_use_a_lot import group_list_by_empty_line
import re

with open('2015 input') as file:
    lines = [line.strip() for line in file]

print(lines)

replacements, start = group_list_by_empty_line(lines)

start = start[0]
print(start)

for i, r in enumerate(replacements):
    replacements[i] = r.split(" => ")

print(replacements)
for r in replacements:
    print(r)

    for i in range(len(start)-len(r[1])+1):
        print(start[i:i+len(r)])