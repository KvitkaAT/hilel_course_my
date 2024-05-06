user_input = input("Enter your number: ")
result = 1
for digit in user_input:  # starts a cycle for multiplying all digits in user input
    result = int(digit) * result
while result > 9:  # if the result > 9
    result_new = 1
    for digit_new in str(result):  # starts the next cycle for multiplying all digits in a string result
        result_new = int(digit_new) * result_new
    result = result_new
print(result)
