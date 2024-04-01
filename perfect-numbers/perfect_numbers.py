def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    sum_divisors = sum(divisores(number))
    if sum_divisors == number:
        return "perfect"
    elif sum_divisors < number:
        return "deficient"
    else:
        return "abundant"


def divisores(number):
    """ Return the divisors of a number.

    :param number: int a positive integer
    :return: list the divisors of the input integer
    """
    list_divisors = []
    for i in range(1, number//2 + 1):
        if number % i == 0:
            list_divisors.append(i)
    return list_divisors
