def add_one(some_list: list) -> list:
    some_string = "".join(str(digit) for digit in some_list)  # converts the list into a string
    string_plus_one = int(some_string) + 1  # adds +1 to a string converted to integer
    return [int(digit) for digit in str(string_plus_one)]  # returns a list of digits


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
    assert add_one([9, 9, 9]) == [1, 0, 0, 0]
    assert add_one([0]) == [1]
    assert add_one([9]) == [1, 0]
    print("ОК")
