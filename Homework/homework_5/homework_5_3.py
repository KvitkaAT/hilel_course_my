import string
import keyword
variable_name = input("Please enter a variable name:")
if variable_name[0].isdigit():  # checks if the first character is digit
    print("False")
elif any(character.isupper() for character in variable_name):  # checks if any character is in upper case
    print("False")
elif any(character in string.punctuation and character != "_" or character == " " for character in variable_name):
    # character in punctuation/space excluding "_"
    print("False")
elif variable_name in keyword.kwlist:  # checks if the variable is a keyword
    print("False")
else:
    print("True")  # if not, print True

