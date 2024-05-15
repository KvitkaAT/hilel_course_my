def square_numbers(numbers: list) -> list:
    """
    Замінює кожне число у списку його квадратом.

    :param numbers: Список чисел.
    :return: Новий список з квадратами чисел.
    """
    return list(map(lambda x: x ** 2, numbers))


if __name__ == "__main__":
    assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
    assert square_numbers([]) == []
    assert square_numbers([7]) == [49]
    print("Ok")
