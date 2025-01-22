import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def pain_calc(wall_height, wall_width, coverage_per_can):
     number_of_cans = math.ceil((wall_height * wall_width) / coverage_per_can)
     print(f"You'll {number_of_cans} cans of paint")


pain_calc(wall_height=test_h, wall_width=test_w, coverage_per_can=coverage)