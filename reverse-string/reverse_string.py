def reverse(text):
    """
    Reverses the given text.

    Args:
        text (str): The text to be reversed.

    Returns:
        str: The reversed text.
    """
    text = list(text)
    text.reverse()
    return ''.join(text)
