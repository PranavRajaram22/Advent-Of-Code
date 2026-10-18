import math

with open("2015 input") as file:
    dimensions = [line.strip() for line in file]

wrapping_paper = 0
ribbon = 0

for dimension in dimensions:
    dim = list(map(int, dimension.split("x")))
    side1area = dim[0] * dim[1]
    side2area = dim[1] * dim[2]
    side3area = dim[2] * dim[0]
    side1perimeter = 2*(dim[0] + dim[1])
    side2perimeter = 2*(dim[1] + dim[2])
    side3perimeter = 2*(dim[2] + dim[0])

    surface_area = 2 * (side1area + side2area + side3area)
    wrapping_paper_slack = min([side1area, side2area, side3area])


    ribbon_slack = math.prod(dim)


    wrapping_paper += surface_area + wrapping_paper_slack
    ribbon += min([side1perimeter, side2perimeter, side3perimeter]) + ribbon_slack



print(f"Part 1: {wrapping_paper}")
print(f"Part 2: {ribbon}")



