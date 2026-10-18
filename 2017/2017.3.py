num = 312051

big_odd_square = 1
big_odd_squareroot = 1


while num > big_odd_square:
    big_odd_squareroot += 2
    big_odd_square = big_odd_squareroot ** 2

small_odd_squareroot = big_odd_squareroot - 2
small_odd_square = small_odd_squareroot**2


sidelength = big_odd_squareroot
part1 = 0
if num == big_odd_square: #bottom corner
    i = big_odd_squareroot
    while i > 1:
        part1 += 2
        i -= 2

else: #not bottom corner
    if small_odd_square < num <= small_odd_square + sidelength-1: #riight side, including top right corner
        mid = ((small_odd_square + 1) + (small_odd_square + sidelength-1))//2

    elif small_odd_square + sidelength-1 < num <= small_odd_square + 2*(sidelength-1): #top side, including top left corner
        mid = (( small_odd_square + sidelength-1) + small_odd_square + 2*(sidelength-1))//2

    elif small_odd_square + 2*(sidelength-1) < num <= small_odd_square + 3*(sidelength-1): #left side, including bottom left corner
        mid = ((small_odd_square + 2*(sidelength-1)) + small_odd_square + 3*(sidelength-1))//2
    else: #bottom side, not including either corner
        mid = ((small_odd_square + 3*(sidelength-1)) + (small_odd_square + 4*(sidelength-1)))//2

    d1 = abs(num-mid)
    d2 = sidelength//2
    part1 = d1+d2

print(f"Part 1: {part1}")


