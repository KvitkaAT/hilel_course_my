def correct_sentence(text: str) -> str:
    if text[-1] != ".":  # if a string doesn't have period at the end
        text = text + "."  # adds "."
    if not text[0].isupper():  # if the first letter in a string is not capitalized
        text = text.capitalize()  # capitalizes the first letter
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence("SEE YOU LATER, ALLigator") == "SEE YOU LATER, ALLigator."
print('ОК')
