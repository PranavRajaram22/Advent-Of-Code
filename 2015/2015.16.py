from itertools import batched

with open("2015 input") as file:
    aunts = [line.strip() for line in file]


for i, aunt in enumerate(aunts):

    aunt = aunt.split(" ")
    aunt.pop(0)
    aunt[0] = int(aunt[0][:-1])
    num = aunt[0]
    notes = aunt[1:]
    for x, note in enumerate(notes):
        notes[x] = note.replace(",", "").replace(":", "")
        try:
            notes[x] = int(notes[x])
        except ValueError:
            pass
    notes = list(batched(notes, 2))
    dict_notes = dict()
    for note in notes:
        dict_notes[note[0]] = note[1]

    is_correct_aunt_part1 = True
    is_correct_aunt_part2 = True

    for key in dict_notes.keys():
        if key == "children" and dict_notes[key] != 3:
            is_correct_aunt_part1 = False
        elif key == "cats" and dict_notes[key] != 7:
            is_correct_aunt_part1 = False
        elif key == "samoyeds" and dict_notes[key] != 2:
            is_correct_aunt_part1 = False
        elif key == "pomeranians" and dict_notes[key] != 3:
            is_correct_aunt_part1 = False
        elif key == "akitas" and dict_notes[key] != 0:
            is_correct_aunt_part1 = False
        elif key == "vizslas" and dict_notes[key] != 0:
            is_correct_aunt_part1 = False
        elif key == "goldfish" and dict_notes[key] != 5:
            is_correct_aunt_part1 = False
        elif key == "trees" and dict_notes[key] != 3:
            is_correct_aunt_part1 = False
        elif key == "cars" and dict_notes[key] != 2:
            is_correct_aunt_part1 = False
        elif key == "perfumes" and dict_notes[key] != 1:
            is_correct_aunt_part1 = False

        if key == "children" and dict_notes[key] != 3:
            is_correct_aunt_part2 = False
        elif key == "cats" and dict_notes[key] <= 7:
            is_correct_aunt_part2 = False
        elif key == "samoyeds" and dict_notes[key] != 2:
            is_correct_aunt_part2 = False
        elif key == "pomeranians" and dict_notes[key] >= 3:
            is_correct_aunt_part2 = False
        elif key == "akitas" and dict_notes[key] != 0:
            is_correct_aunt_part2 = False
        elif key == "vizslas" and dict_notes[key] != 0:
            is_correct_aunt_part2 = False
        elif key == "goldfish" and dict_notes[key] >= 5:
            is_correct_aunt_part2 = False
        elif key == "trees" and dict_notes[key] <= 3:
            is_correct_aunt_part2 = False
        elif key == "cars" and dict_notes[key] != 2:
            is_correct_aunt_part2 = False
        elif key == "perfumes" and dict_notes[key] != 1:
            is_correct_aunt_part2 = False

    if is_correct_aunt_part1:
        print(f"Part 1: {num}")
    if is_correct_aunt_part2:
        print(f"Part 2: {num}")
