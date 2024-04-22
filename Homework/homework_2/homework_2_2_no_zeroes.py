user_input = input("Please enter a five-digit number:")
num = int(user_input)
a = str(num % 10)  # returns the fifth digit and turns it into a string
b = str(num // 10 % 10)  # returns the fourth digit and turns it into a string
c = str(num // 100 % 10)  # returns the third digit and turns it into a string
d = str(num // 1000 % 10)  # returns the second digit and turns it into a string
e = str(num // 10000)  # returns the first digit and turns it into a string
reversed_number = a + b + c + d + e  # returns the sum of strings
print(int(reversed_number))
