#tracking d, switch to track a for actual input

signals = dict()

with open('2015 input') as file:
    circuit = [line.strip() for line in file]


def findVar(var): #ultimately want to find d/a
    for line in circuit:
        line = line.split(' ')
        for i, x in enumerate(line):
            try:
                line[i] = int(x)
            except ValueError:
                pass

        if line[-1] == var:
            if len(line) == 3: #simple assignment
                if type(line[0]) == int:
                    signals[var] = line[0]
                else:
                    try:
                        signals[var] = signals[line[0]]
                    except KeyError:
                        findVar(line[0])
                        signals[var] = signals[line[0]]


            elif len(line) == 4: #not
                mask = int('0b1111111111111111',2)

                if type(line[1]) == int:
                    signals[var] = ~line[1] & mask

                else:
                    try:
                        signals[var] = ~signals[line[1]] & mask
                    except KeyError:
                        findVar(line[1])
                        signals[var] = ~signals[line[1]] & mask

            elif line[1] == 'AND':

                if type(line[0]) == int:
                    var1 = line[0]
                else:
                    try:
                        var1 = signals[line[0]]
                    except KeyError:
                        findVar(line[0])
                        var1 = signals[line[0]]

                if type(line[2]) == int:
                    var2 = line[2]
                else:
                    try:
                        var2 = signals[line[2]]
                    except KeyError:
                        findVar(line[2])
                        var2 = signals[line[2]]

                signals[var] = var1 & var2


            elif line[1] == "OR":
                if type(line[0]) == int:
                    var1 = line[0]
                else:
                    try:
                        var1 = signals[line[0]]
                    except KeyError:
                        findVar(line[0])
                        var1 = signals[line[0]]

                if type(line[2]) == int:
                    var2 = line[2]
                else:
                    try:
                        var2 = signals[line[2]]
                    except KeyError:
                        findVar(line[2])
                        var2 = signals[line[2]]

                signals[var] = var1 | var2


            elif line[1] == "LSHIFT":
                if type(line[0]) == int:
                    var1 = line[0]
                else:
                    try:
                        var1 = signals[line[0]]
                    except KeyError:
                        findVar(line[0])
                        var1 = signals[line[0]]

                if type(line[2]) == int:
                    var2 = line[2]
                else:
                    try:
                        var2 = signals[line[2]]
                    except KeyError:
                        findVar(line[2])
                        var2 = signals[line[2]]

                signals[var] = var1 << var2


            elif line[1] == "RSHIFT":
                if type(line[0]) == int:
                    var1 = line[0]
                else:
                    try:
                        var1 = signals[line[0]]
                    except KeyError:
                        findVar(line[0])
                        var1 = signals[line[0]]

                if type(line[2]) == int:
                    var2 = line[2]
                else:
                    try:
                        var2 = signals[line[2]]
                    except KeyError:
                        findVar(line[2])
                        var2 = signals[line[2]]

                signals[var] = var1 >> var2


findVar('a')
print(f"Part 1: {signals['a']}")

a = signals['a']

signals = dict()

signals['b'] = a

findVar('a')
print(f"Part 2: {signals['a']}")