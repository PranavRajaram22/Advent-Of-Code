with open('2015 input') as file:
    stringliterals = [line.strip() for line in file]



def memoryLength(string):
    string = string[1:-1] #to remove the outer quotations

    i = 0
    memoryString = ""
    while i < len(string):
        if string[i] != '\\':
            memoryString += string[i]
            i += 1
        else:
            if string[i:i+2] == '\\\\':
                memoryString += '\\'
                i += 2
            elif string[i:i+2] == '\\\"':
                memoryString += "\""
                i += 2
            elif string[i:i+2] == "\\x":
                integer = int(string[i+2:i+4], 16)
                memoryString += chr(integer)
                i += 4

    return len(memoryString)

memoryLength(stringliterals[3])

literalLengthsum = 0
memoryLengthsum = 0

for string in stringliterals:
    literalLengthsum += len(string)
    memoryLengthsum += memoryLength(string)

print(f"Part 1: {literalLengthsum - memoryLengthsum}")


stringMemories = stringliterals
def literalLength(string):
    stringLiteral = "\""

    for char in string:
        if char == "\\":
            stringLiteral += "\\\\"
        elif char == "\"":
            stringLiteral += "\\\""
        else:
            stringLiteral += char
    stringLiteral += "\""
    return len(stringLiteral)


literalLength(stringMemories[3])

literalLengthsum = 0
memoryLengthsum = 0

for string in stringMemories:
    memoryLengthsum += len(string)
    literalLengthsum += literalLength(string)

print(f"Part 2: {literalLengthsum - memoryLengthsum}")