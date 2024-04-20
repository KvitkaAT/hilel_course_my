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