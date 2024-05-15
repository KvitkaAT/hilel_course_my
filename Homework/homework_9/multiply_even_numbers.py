def multiply_even_numbers(numbers: list) -> list:
    """
    Помножує всі парні числа у списку на 2.

    :param numbers: Список чисел.
    :return: Новий список з парними числами, помноженими на 2.
    """
    result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
    return result


if __name__ == "__main__":
    assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]
    assert multiply_even_numbers([1, 3, 5, 7, 9]) == []
    assert multiply_even_numbers([]) == []
    assert multiply_even_numbers([2]) == [4]
    print("Ok")


