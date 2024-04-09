codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
         'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}


def value(colors: list) -> int:
    """
    Calculates the value of a resistor based on the color bands.

    Args:
        colors (list): A list of color codes representing the color bands of the resistor.

    Returns:
        int: The numerical value of the resistor.

    """
    color_one = colors[0]
    color_two = colors[1]

    return int(str(codes[color_one]) + str(codes[color_two]))
