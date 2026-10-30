from collections import deque

outputs = []
def run(intcode):
    i = 0
    while True:
        opcode = int(str(intcode[i])[-2:])
        parameters = deque(map(int, list(str(intcode[i])[:-2])))
        if opcode == 1:
            while len(parameters) < 3:
                parameters.appendleft(0)
            parameters.reverse()

            inputs = []
            paraidx = 0
            j = i+1

            while j < i+1+2:
                if parameters[paraidx] == 0: #position mode
                    inputs.append(intcode[intcode[j]])
                else: #immediate mode:
                    inputs.append(intcode[j])
                paraidx += 1
                j += 1

            output = sum(inputs)
            if parameters[paraidx] == 0: #position mode
                intcode[intcode[j]] = output
            else:
                intcode[j] = output

            i += 4

        elif opcode == 2:
            while len(parameters) < 3:
                parameters.appendleft(0)
            parameters.reverse()

            inputs = []
            paraidx = 0
            j = i + 1

            while j < i + 1 + 2:
                if parameters[paraidx] == 0:  # position mode
                    inputs.append(intcode[intcode[j]])
                else:  # immediate mode:
                    inputs.append(intcode[j])
                paraidx += 1
                j += 1
            output = 1
            for k in inputs:
                output *= k
            if parameters[paraidx] == 0:  # position mode
                intcode[intcode[j]] = output
            else:
                intcode[j] = output

            i += 4

        elif opcode == 3:
            while len(parameters) < 1:
                parameters.appendleft(0)
            parameters.reverse()
            if parameters[0] == 0: #position mode:
                intcode[intcode[i+1]] = inp
            else: #immediate mode:
                intcode[i+1] = inp

            i += 2

        elif opcode == 4:
            while len(parameters) < 1:
                parameters.appendleft(0)
            parameters.reverse()

            if parameters[0] == 0: #position mode:
                outputs.append(intcode[intcode[i+1]])
            else: #immediate mode:
                outputs.append(intcode[i+1])

            i += 2

        elif opcode == 5:
            while len(parameters) < 2:
                parameters.appendleft(0)
            parameters.reverse()

            if parameters[0] == 0: #position mode for first arg
                arg = intcode[intcode[i+1]]
            else:
                arg = intcode[i+1]

            if arg != 0: #jump
                if parameters[1] == 0: #position mode for jump
                    i = intcode[intcode[i+2]]
                else:
                    i = intcode[i+2]


            else:
                i += 3

        elif opcode == 6:
            while len(parameters) < 2:
                parameters.appendleft(0)
            parameters.reverse()

            if parameters[0] == 0:  # position mode for first arg
                arg = intcode[intcode[i + 1]]
            else:
                arg = intcode[i + 1]

            if arg == 0:  # jump
                if parameters[1] == 0:  # position mode for jump
                    i = intcode[intcode[i + 2]]
                else:
                    i = intcode[i + 2]
            else:
                i += 3

        elif opcode == 7:

            while len(parameters) < 3:
                parameters.appendleft(0)
            parameters.reverse()

            if parameters[0] == 0:
                arg1 = intcode[intcode[i+1]]
            else:
                arg1 = intcode[i+1]

            if parameters[1] == 0:
                arg2 = intcode[intcode[i + 2]]
            else:
                arg2 = intcode[i + 2]

            if parameters[2] == 0:
                if arg1 < arg2:
                    intcode[intcode[i+3]] = 1
                else:
                    intcode[intcode[i+3]] = 0
            else:
                if arg1 < arg2:
                    intcode[i+3] = 1
                else:
                    intcode[i+3] = 0


            i += 4
        elif opcode == 8:
            while len(parameters) < 3:
                parameters.appendleft(0)
            parameters.reverse()

            if parameters[0] == 0:
                arg1 = intcode[intcode[i + 1]]
            else:
                arg1 = intcode[i + 1]

            if parameters[1] == 0:
                arg2 = intcode[intcode[i + 2]]
            else:
                arg2 = intcode[i + 2]

            if parameters[2] == 0:
                if arg1 == arg2:
                    intcode[intcode[i + 3]] = 1
                else:
                    intcode[intcode[i + 3]] = 0
            else:
                if arg1 == arg2:
                    intcode[i + 3] = 1
                else:
                    intcode[i + 3] = 0

            i += 4
        elif opcode == 99:
            return intcode

with open('2019 input') as file:
    intc = list(map(int, file.readline().strip().split(",")))

inp = 1
run(intc.copy())
print(f"Part 1: {outputs[-1]}")

inp = 5
outputs = []
run(intc.copy())
print(f"Part 2: {outputs[-1]}")