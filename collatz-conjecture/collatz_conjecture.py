count = 0


def steps(number):
    global count
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number % 2 == 0:
        count += 1
        print(number)
        return steps(number // 2)
    if number == 1:
        count += 1
        print(number)
        return count
    else:
        count += 1
        print(number)
        return steps(3 * number + 1)
