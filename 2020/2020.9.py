preamble_length = 25

with open('2020 input') as file:
    lines = [int(line.strip()) for line in file]


preamble = lines[:preamble_length]

i = preamble_length

wrongnum = 0
wrongnumidx = 0
while True:
    num = lines[i]
    found = False
    for idx in range(len(preamble)):
        for jdx in range(len(preamble)):
            if preamble[idx] + preamble[jdx] == num and idx != jdx:
                found = True

    if not found:
        wrongnum = num
        wrongnumidx = i
        print(f"Part 1: {num}")

        break
    if found:

        i += 1
        preamble = lines[i-preamble_length:i]



for length in range(1, wrongnumidx+1):
    for i in range(0, wrongnumidx-length+1):
        x = lines[i:i+length]
        if sum(x) == wrongnum:
            print(f"Part 2: {max(x) + min(x)}")
            break

