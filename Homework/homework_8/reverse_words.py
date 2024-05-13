def reverse_words(sentence: str) -> str:
    split_sentence = sentence.split(" ")
    return " ".join(word[:: -1] for word in split_sentence)


if __name__ == "__main__":
    assert reverse_words("Hello world") == "olleH dlrow"
    assert reverse_words("Python is fun") == "nohtyP si nuf"
    assert reverse_words("Quick brown fox") == "kciuQ nworb xof"
    assert reverse_words("Just a test") == "tsuJ a tset"
    assert reverse_words("123 456") == "321 654"
    print("Ok")
