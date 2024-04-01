def convert(number):
    """ Convert a number to a string, the contents of which depend on the number.

    :param number: int a positive integer
    :return: str the raindrop sounds or the number as a string
    """
    raindrop_sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    raindrop_string = ''
    for key, value in raindrop_sounds.items():
        if number % key == 0:
            raindrop_string += value
    return raindrop_string if raindrop_string else str(number)
