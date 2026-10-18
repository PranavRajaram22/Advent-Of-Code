import json

with open('2015 input') as file:
    text = file.readlines()[0]

numbers = []

currnum = ""

for i in range(len(text)):
    if text[i] == '-' and len(currnum) == 0:
        currnum += '-'
    elif text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        currnum += text[i]

    elif len(currnum) > 0:
        numbers.append(currnum)
        currnum = ""

while '-' in numbers:
    numbers.remove('-')

numbers = list(map(int, numbers))
print(f"Part 1: {sum(numbers)}")

text = json.loads(text)

def parse(text):
    count = 0
    if type(text) == list:
        for element in text:
            if type(element) not in [list, dict]:
                if type(element) == int:
                    count += int(element)
            else:
                count += parse(element)

    elif type(text) == dict:
        if "red" not in text.keys() and "red" not in text.values():

            for key in text.keys():
                if type(key) not in [list, dict]:
                    if type(key) == int:
                        count += int(key)
                else:
                    count += parse(key)

            for value in text.values():
                if type(value) not in [list, dict]:
                    if type(value) == int:
                        count += int(value)
                else:
                    count += parse(value)

    return count

print(f"Part 2: {parse(text)}")

