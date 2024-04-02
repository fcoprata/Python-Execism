def is_isogram(string):
    """
    Check if a given string is an isogram.

    An isogram is a word or phrase without any repeating letters.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    string = string.lower()
    for char in string:
        if char.isalpha() and string.count(char) > 1:
            return False
    return True
