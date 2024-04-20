user_input = input("Please enter a four-digit number:")
num = int(user_input)
div, mod = divmod(num, 100)
a = div // 10  #  returns the first digit
b = div % 10  # returns the second digit
c = mod // 10  # returns the third digit
d = mod % 10  # returns the fourth digit
print(a)
print(b)
print(c)
print(d)
