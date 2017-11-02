def WordFrequency(lyrics):
    def toChars(lyrics):
        lyrics = lyrics.lower()
        words = ''
        for i in lyrics:
            if i in 'abcdefghijklmnopqrstuvwxyz ':
                words += i
        return words

    def SortWords(words):
        word_frequency = {}
        for i in words:
            word_frequency[i] += 1

        return word_frequency

    return SortWords(toChars(lyrics))


print(WordFrequency(input("Enter lyrics: ")))
