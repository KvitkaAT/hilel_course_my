import string
user_input = "a-c"
first_letter_index = string.ascii_letters.find(user_input[0])  # finds the index of the first letter
last_letter_index = string.ascii_letters.find(user_input[-1])  # finds the index of the last letter
print(string.ascii_letters[first_letter_index:last_letter_index + 1])  # displays all letters between the first & last
