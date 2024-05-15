def factorial(num: int) -> int | str:
    """
    Обчислює факторіал числа num.

    :param num: Ціле число.
    :return: Факторіал числа num.
    """
    if num < 0:
        return "Please enter a positive number."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(-5) == "Please enter a positive number."
    assert factorial(10) == 3628800
    print("Ok")


