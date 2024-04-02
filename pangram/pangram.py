def is_pangram(sentence):
    """
    Check if a sentence is a pangram.

    Args:
        sentence (str): The sentence to be checked.

    Returns:
        bool: True if the sentence is a pangram, False otherwise.
    """
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True
