def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    translated_words = []

    for word in words:
        if word[0] in vowels:
            translated_word = word + 'ay'
        else:
            consonant_cluster = ''
            for i in range(len(word)):
                if word[i] not in vowels:
                    consonant_cluster += word[i]
                else: break
            translated_word = word[len(consonant_cluster):] + consonant_cluster + 'ay'

        translated_words.append(translated_word)

    return ' '.join(translated_words)
