def square(number):
    """
    Calculates the number of grains on a given square of a chessboard.

    Args:
        number (int): The square number on the chessboard (1-64).

    Returns:
        int: The number of grains on the given square.

    Raises:
        ValueError: If the number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("Number must be between 1 and 64")
    return 2**(number-1)


def total():
    """
    Calculates the total number of grains on the entire chessboard.

    Returns:
        int: The total number of grains on the chessboard.
    """
    return sum(square(i) for i in range(1, 65))
