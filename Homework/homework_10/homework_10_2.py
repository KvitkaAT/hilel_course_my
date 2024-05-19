def first_word(text: str) -> str:
    """ Пошук першого слова """
    text_modified = text.strip(",. ")  # deletes ",. " in the string
    first_word_string = ""  # creates an empty string
    for character in text_modified:  # loops through all string characters
        if character in (" ,."):  # if character is not a letter, break the loop
            break
        first_word_string += character  # jumps to another character in a string
    return first_word_string


if __name__ == "__main__":
    assert first_word("Hello world") == "Hello"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("don't touch it") == "don't"
    assert first_word(".., and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print('OK')



