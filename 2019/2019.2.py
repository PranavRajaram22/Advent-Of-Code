with open('2019 input') as file:
    masterintcode = (list(map(int, file.readline().split(","))))

#opcodes
#1 -> add
#2 -> multiply
#99 -> halt

intcode = masterintcode.copy()

def run(intcode):
    i = 0
    while True:
        opcode = intcode[i]
        if opcode == 1:
            pos1, pos2, pos3 = intcode[i + 1], intcode[i + 2], intcode[i + 3]
            arg1, arg2 = intcode[pos1], intcode[pos2]
            output = arg1 + arg2
            intcode[pos3] = output
            i += 4
        elif opcode == 2:
            pos1, pos2, pos3 = intcode[i + 1], intcode[i + 2], intcode[i + 3]
            arg1, arg2 = intcode[pos1], intcode[pos2]
            output = arg1 * arg2
            intcode[pos3] = output
            i += 4
        elif opcode == 99:
            break


intcode[1] = 12
intcode[2] = 2
run(intcode)
print(f"Part 1: {intcode[0]}")

for noun in range(100):
    for verb in range(100):
        intcode = masterintcode.copy()
        intcode[1] = noun
        intcode[2] = verb
        run(intcode)
        output = intcode[0]
        if output == 19690720:
            print(f"Part 2: {noun*100 + verb}")
            exit()




