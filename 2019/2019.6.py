
graph = dict()


with open('2019 input') as file:
    orbits = [line.strip() for line in file]

planets = set()
for orbit in orbits:
    center, orbital = orbit.split(")")
    graph[orbital] = center
    planets.add(center)
    planets.add(orbital)


def rec(planet):
    if graph[planet] == 'COM':
        return 1
    else:
        return 1 + rec(graph[planet])

count = 0

for planet in planets:
    if planet != 'COM':
        count += rec(planet)

print(f"Part 1: {count}")

path_from_you_to_COM = []
path_from_santa_to_COM = []

def rec2(planet, is_you=True):
    if planet != 'COM':
        if is_you:
            path_from_you_to_COM.append(planet)
        else:
            path_from_santa_to_COM.append(planet)
        rec2(graph[planet], is_you)
    else:
        if is_you:
            path_from_you_to_COM.append('COM')
        else:
            path_from_santa_to_COM.append('COM')


rec2('YOU', is_you=True)
rec2('SAN', is_you=False)


for i, planet in enumerate(path_from_you_to_COM):
    if planet in path_from_santa_to_COM:
        j = path_from_santa_to_COM.index(planet)
        print(f"Part 2: {i+j-2}")
        break
