chars = "abcdefghijklmnopqrstuvwxyz"


def rotate(text, key):
    """
    Applies a rotational cipher to the given text using the specified key.

    Args:
        text (str): The text to be encrypted.
        key (int): The rotation key.

    Returns:
        str: The encrypted text.

    Example:
        >>> rotate("Hello, World!", 13)
        'Uryyb, Jbeyq!'
    """
    newchars = chars[key:] + chars[:key]
    trans = str.maketrans(chars + chars.upper(), newchars + newchars.upper())
    return text.translate(trans)
