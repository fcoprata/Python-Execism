def steps(number):
    """
    Calculates the number of steps required to reach 1 using the Collatz Conjecture.

    Args:
        number (int): The starting number.

    Returns:
        int: The number of steps required to reach 1.

    Raises:
        ValueError: If the input number is less than 1.
    """
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    counter = 0
    while number > 1:
        number = 3 * number + 1 if number % 2 else number // 2
        counter += 1
    return counter
