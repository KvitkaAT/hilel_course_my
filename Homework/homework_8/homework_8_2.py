import string


def is_palindrome(text: str) -> bool:
    text_modified = "".join(char for char in text.lower() if char not in string.punctuation and char != " ")
    return text_modified == text_modified[:: -1]


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('0P') == False
    assert is_palindrome('a.') == True
    assert is_palindrome('aurora') == False
    print("ОК")
