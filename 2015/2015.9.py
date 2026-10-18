from itertools import permutations

with open('2015 input') as file:
    distances = [line.strip().split(" ") for line in file]


for i, distance in enumerate(distances):
    distance.pop(1)
    distance.pop(2)
    distance[-1] = int(distance[-1])
    distances[i] = distance


firstCity = distances[0][0]

cities = set()
cities.add(firstCity)
for distance in distances:
    if distance[0] == firstCity:
        cities.add(distance[1])
perms = list(permutations(cities))
lengths = set()

for perm in perms:
    totalDistance = 0
    for i in range(len(perm)-1):
        city1 = perm[i]
        city2 = perm[i+1]
        for distance in distances:
            if (distance[0] == city1 and distance[1] == city2) or (distance[0] == city2 and distance[1] == city1):
                totalDistance += distance[2]
    lengths.add(totalDistance)

print(f"Part 1: {min(lengths)}")
print(f"Part 2: {max(lengths)}")

