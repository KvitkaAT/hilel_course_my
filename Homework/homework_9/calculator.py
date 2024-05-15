def calculator(num1: int | float, num2: int | float, operation: str) -> int | float | str:
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """
    if operation == "add":
        result = num1 + num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by 0 is not allowed."
        result = num1 / num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "subtract":
        result = num1 - num2
    else:
        return "Unknown operation. Please choose the following: 'add', 'divide', 'multiply', 'subtract'."
    return result


if __name__ == "__main__":
    assert calculator(5, 3, 'add') == 8
    assert calculator(5, 3, 'multiply') == 15
    assert calculator(15, 3, 'divide') == 5
    assert calculator(5, 0, 'divide') == "Division by 0 is not allowed."
    assert calculator(5, 3, 'subtract') == 2
    assert calculator(5, 3, 'davide') == "Unknown operation. Please choose the following: 'add', 'divide', 'multiply', 'subtract'."
    print('OK')


