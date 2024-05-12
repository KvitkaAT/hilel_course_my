def sum_of_digits(number: int) -> int:
    number_string = str(abs(number))
    result = 0
    for digit in number_string:
        result = int(digit) + result
    return result


if __name__ == "__main__":
    assert sum_of_digits(123) == 6
    assert sum_of_digits(-456) == 15
    assert sum_of_digits(789) == 24
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-9876) == 30
    print("Ok")
