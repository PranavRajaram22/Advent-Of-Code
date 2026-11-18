c = 0
def isPossible(game):
    game = game.split(";")
    id, game[0] = game[0].split(":")
    id = id.split(" ")[1]
    groups = game


    for group in groups:
        group = group.split(', ')
        for i, c in enumerate(group):
            group[i] = c.split(" ")
            try:
                group[i].pop(group[i].index(''))
            except ValueError:
                pass

        for marbles in group:
            if marbles[1] == 'blue' and int(marbles[0]) > 14:
                return 0
            elif marbles[1] == 'red' and int(marbles[0]) > 12:
                return 0
            elif marbles[1] == 'green' and int(marbles[0]) > 13:
                return 0

    return int(id)

def minMarbles(game):
    game = game.split(";")
    id, game[0] = game[0].split(":")
    id = id.split(" ")[1]
    groups = game


    for j, group in enumerate(groups):
        group = group.split(', ')
        for i, c in enumerate(group):
            group[i] = c.split(" ")
            try:
                group[i].pop(group[i].index(''))
            except ValueError:
                pass

        groups[j] = group

    minRed, minGreen, minBlue = 0, 0, 0
    for group in groups:
        for marble in group:
            num, color = int(marble[0]), marble[1]
            if color == 'blue':
                minBlue = max(num, minBlue)
            elif color == 'red':
                minRed = max(num, minRed)
            elif color == 'green':
                minGreen = max(num, minGreen)

    return minRed*minBlue*minGreen


with open('2023 input') as file:
    games = [line.strip() for line in file]

for game in games:
    c += isPossible(game)

print(f"Part 1: {c}")

print(f'Part 2: {sum([minMarbles(game) for game in games])}')