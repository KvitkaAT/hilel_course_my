while True:
    first_number = int(input("Enter a number: "))  # input the first number
    operation = input("Enter an operation: +, -, *, /: ")  # input the operation
    while operation not in ["+", "-", "*", "/"]:  # if the operation not in the list
        print("Unknown operation. Use one of the following operations: +, -, *, /")
        operation = input("Enter an operation: +, -, *, /: ")
    second_number = int(input("Enter a number: "))
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
    further_action = input("Enter 'Yes' or 'Y' to make more calculations: ")  # input to proceed
    if further_action.lower() != "yes" and further_action.lower() != "y":  # if not yes/y, end the program
        print("End")
        break

