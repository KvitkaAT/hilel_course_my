first_number = int(input("Please enter a number:"))
operation = input("Enter an operation: +, -, *, /:")
second_number = int(input("Please enter a number:"))
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Division by zero is not allowed.")
else:
    print("Unknown operation. Please enter one of the following operations: +, -, *, /:")
