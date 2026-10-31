with open('2020 input') as file:
    entries = [line.strip() for line in file]

entries = list(map(int, entries))

for entry in entries:
    if 2020-entry in entries:
        print(f"Part 1: {entry * (2020-entry)}")
        break


for i, entry1 in enumerate(entries):
    for j, entry2 in enumerate(entries):
        for k, entry3 in enumerate(entries):
            if entry1 + entry2 + entry3 == 2020 and i != j and i != k and j != k:
                print(f"Part 2: {entry1 * entry2 * entry3}")
                exit()


