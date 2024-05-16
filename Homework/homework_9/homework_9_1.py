def popular_words(text: str, words: list) -> dict:
    return {word: text.lower().split().count(word) for word in words}  # converts the string into lower case
#  splits the string into a list of words, counts the word number in a list, returns a dictionary key-value


if __name__ == "__main__":
    assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                         ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    print("OK")
