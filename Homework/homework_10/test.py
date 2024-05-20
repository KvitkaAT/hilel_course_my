text = "Hello World"
text_modified = text.strip("., ")
first_word = ""
for character in text_modified:
    if character == " " or character == "." or character == ",":
        break
    first_word += character
print(first_word)

