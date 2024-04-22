user_input = input("Please enter a five-digit number:")
num = int(user_input)
# a five-digit number can be written as follows: a * 10000 + b * 1000 + c * 100 + d * 10 + e.
# To reverse a number, we will use the reverse digit order.
a = (num % 10) * 10000  # returns the fifth digit and places it first
b = (num // 10 % 10) * 1000  # returns the fourth digit and places it second
c = (num // 100 % 10) * 100  # returns the third digit and places it third
d = (num // 1000 % 10) * 10  # returns the second digit and places it fourth
e = (num // 10000)  # returns the first digit and places it fifth
reversed_number = a + b + c + d + e  # returns the reversed five-digit number
print(reversed_number)
