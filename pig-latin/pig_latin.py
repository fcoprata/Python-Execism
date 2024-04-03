def translate(text):
    """
    Translates a given text into Pig Latin.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The translated text in Pig Latin.
    """
    return ' '.join([translate_word(word) for word in text.split()])


def translate_word(word):
    """
    Translates a single word into Pig Latin.

    Args:
        word (str): The word to be translated.

    Returns:
        str: The translated word in Pig Latin.
    """
    for vowel in ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']:
        if word.startswith(vowel):
            return word + 'ay'
    for consonant in ['squ', 'sch', 'thr', 'qu', 'ch', 'th', 'y', 'rh']:
        if word.startswith(consonant):
            return word[len(consonant):] + consonant + 'ay'

    return word[1:] + word[0] + 'ay'
