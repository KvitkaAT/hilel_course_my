import string
user_input = input("Please enter your text: ")
no_punctuation_input = "".join(char for char in user_input if char not in string.punctuation)  # deletes the punctuation
no_spaces_input = no_punctuation_input.title().replace(" ", "")  # deletes spaces & capitalizes 1st words
hashtag = "#" + no_spaces_input
if len(hashtag) <= 140:  # if hashtag is <=140, display in full
    print(hashtag)
else:
    print(hashtag[:140])  # if not, display the first 140 symbols
