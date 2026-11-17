with open('2022 input') as file:
    games = [line.strip().split(" ") for line in file]

shapescore = {'X': 1, "Y":2, "Z":3}
score = 0

'''
A = X = Rock
B = Y = Paper
C = Z = Scissors

'''
for game in games:
    opp, you = game
    score += shapescore[you]
    if opp == 'A': #opponent plays rock
        if you == 'X':
            score += 3
        elif you == 'Y':
            score += 6
        else:
            score += 0

    elif opp == 'B': #opponent plays paper
        if you == 'X':
            score += 0
        elif you == 'Y':
            score += 3
        else:
            score += 6

    elif opp == 'C': #opponent plays scissors
        if you == 'X':
            score += 6
        elif you == 'Y':
            score += 0
        else:
            score += 3



print(f'Part 1: {score}')
score = 0


'''
A = Rock
B = Paper
C = Scissors

X = Lose
Y = Tie
Z = Win

'''
for game in games:
    opp, result = game

    if opp == 'A': #rock
        if result == 'X':
            score += 0 + shapescore['Z']
        elif result == 'Y':
            score += 3 + shapescore['X']
        else:
            score += 6 + shapescore['Y']

    elif opp == 'B':
        if result == 'X':
            score += 0 + shapescore['X']
        elif result == 'Y':
            score += 3 + shapescore['Y']
        else:
            score += 6 + shapescore['Z']

    elif opp == 'C':
        if result == 'X':
            score += 0 + shapescore['Y']
        elif result == 'Y':
            score += 3 + shapescore['Z']
        else:
            score += 6 + shapescore['X']


print(f"Part 2: {score}")
