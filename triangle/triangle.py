def is_valid_triangle(sides: list):
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[2] + sides[1] > sides[0]:
        return True
    else:
        return False


def equilateral(sides: list):
    return len(set(sides)) == 1 and is_valid_triangle(sides)


def isosceles(sides):
    return len(set(sides)) <= 2 and is_valid_triangle(sides)


def scalene(sides):
    return len(set(sides)) == 3 and is_valid_triangle(sides)