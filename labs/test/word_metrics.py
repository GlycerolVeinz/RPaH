def answer():
    """Answer for the question.

    :return set:
    """
    return set(["dolor", "sit", "sodales"])


def longest_word(string: str):
    """Find the longest word in the given string, and its length.

    A 'word' is a sequence of characters other than spaces, which has non-zero length.

    If the given string contains no words, (0, '') should be returned.

    If multiple words are of the longest length, return the one that occurs first in the string.

    :param string: The string to find longest word in.
    :type string: str
    :return: A tuple (length of the longest word, the longest word).
    :rtype: tuple
    """

    best_length = 0
    best_word = ""

    if (len(string) == 0):
        return best_length, best_word
    else:
        words = string.split(" ")
        best_word = words[0]
        for w in words:
            if len(w) > len(best_word):
                best_word = w
            else:
                pass
        return (len(best_word), best_word)

    


if __name__ == "__main__":
    pass