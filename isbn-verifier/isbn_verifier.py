def is_valid(isbn):
    """
    Check if the given ISBN (International Standard Book Number) is valid.

    Args:
        isbn (str): The ISBN to be validated.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10: return False
    if isbn[-1] == 'X': isbn[-1] = "10"
    try:
        total = sum(i * n for i, n in enumerate(isbn))
    except ValueError: return False
    return total % 11 == 0
