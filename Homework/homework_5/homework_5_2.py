import string
user_input = input("Please enter your text: ")
no_punctuation_input = "".join(char for char in user_input.title() if char not in string.punctuation and char != " ")
# capitalizes each word in user input + deletes the punctuation
hashtag = "#"+no_punctuation_input  # adds # to the modified user input
if len(hashtag) <= 140:  # if hashtag is <=140, display in full
    print(hashtag)
else:
    print(hashtag[:141])  # if hashtag >140, display the first 140 symbols
