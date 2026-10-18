with open('2016 input') as file:
    triangles = [line.strip().split(" ") for line in file]


c = 0

for i, triangle in enumerate(triangles):
    while "" in triangle:
        triangle.remove("")

    triangle = list(map(int, triangle))
    triangles[i] = triangle
    hyp = max(triangle)
    minside = min(triangle)
    otherside = sum(triangle)-hyp-minside

    if minside + otherside > hyp:
        c += 1

print(f"Part 1: {c}")

groups = []

tri1 = []
tri2 = []
tri3 = []
for triangle in triangles:
    if len(tri1) < 3:
        tri1.append(triangle[0])
        tri2.append(triangle[1])
        tri3.append(triangle[2])

    if len(tri1) == 3:
        groups.append(tri1)
        groups.append(tri2)
        groups.append(tri3)
        tri1 = []
        tri2 = []
        tri3 = []

triangles = groups
c = 0
for i, triangle in enumerate(triangles):
    triangles[i] = triangle
    hyp = max(triangle)
    minside = min(triangle)
    otherside = sum(triangle)-hyp-minside

    if minside + otherside > hyp:
        c += 1

print(f"Part 2: {c}")