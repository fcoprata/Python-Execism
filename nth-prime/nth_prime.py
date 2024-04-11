def isPrime(number):
    """
    Check if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime(number):
    """
    Returns the nth prime number.

    Args:
        number (int): The position of the prime number to be returned.

    Returns:
        int: The nth prime number.

    Raises:
        ValueError: If the input number is 0.

    """
    if number == 0:
        raise ValueError('there is no zeroth prime')
    i = 2
    count = 0
    while True:
        if isPrime(i):
            count += 1
        if count == number:
            break
        i += 1
    return i
