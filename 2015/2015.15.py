with open('2015 input') as file:
    ingredients = [line.strip() for line in file]

for i, ingredient in enumerate(ingredients):
    while "," in ingredient:
        ingredient = ingredient.replace(",", "")
    ingredient = ingredient.split(" ")
    ingredient.pop(1)
    ingredient.pop(2)
    ingredient.pop(3)
    ingredient.pop(4)
    ingredient.pop(5)
    ingredient.pop(0)

    ingredient = list(map(int, ingredient))
    #capacity, durability, flavour, text, calories
    ingredients[i] = ingredient

maxscore_part1 = 1
maxscore_part2 = 1
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):

            l = 100 - i - j - k

            first = ingredients[0]
            new_first = [first[z] * i for z in range(len(first))]

            second = ingredients[1]
            new_second = [second[z] * j for z in range(len(second))]

            third = ingredients[2]
            new_third = [third[z] * k for z in range(len(third))]

            fourth = ingredients[3]
            new_fourth = [fourth[z] * l for z in range(len(fourth))]

            score = 1

            calories = new_first[-1] + new_second[-1] + new_third[-1] + new_fourth[-1]
            for x in range(4):
                score *= max(0, new_first[x] + new_second[x] + new_third[x] + new_fourth[x])

            if score > maxscore_part1:
                maxscore_part1 = score

            if calories == 500:
                if score > maxscore_part2:
                    maxscore_part2 = score

print(f"Part 1: {maxscore_part1}")
print(f"Part 2: {maxscore_part2}")

