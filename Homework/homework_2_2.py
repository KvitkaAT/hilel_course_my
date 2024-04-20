user_input = input("Please enter a five-digit number:")
num = int(user_input)

#  1) extract each digit using // and % 2) change the type to string to handle 0 digit
a = str(num % 10)
b = str(num // 10 % 10)
c = str(num // 100 % 10)
d = str(num // 1000 % 10)
e = str(num // 10000)
reversed_num = a + b + c + d + e
print(reversed_num)

# solves the 0 problem