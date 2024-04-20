user_input = input("Please enter a four-digit number:")
num = int(user_input)
a = num // 1000  # returns the first digit
b = (num // 100) % 10  # returns the second digit
c = (num // 10) % 10  # returns the third digit
d = num % 10  # returns the fourth digit
print(a)
print(b)
print(c)
print(d)

# variant with a divmod

user_input = input("Please enter a four-digit number:")
num = int(user_input)
div, mod = divmod(num, 100)
a = div // 10
b = div % 10
c = mod // 10
d = mod % 10
print(a)
print(b)
print(c)
print(d)
