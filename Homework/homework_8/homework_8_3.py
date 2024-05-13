def find_unique_value(some_list: list) -> int | float | str:
    unique_list = [number for number in some_list if some_list.count(number) == 1]  # creates a list of unique elements
    if not unique_list:  # if the list of unique values is empty
        return "No unique element found"
    return unique_list[0]


if __name__ == "__main__":
    assert find_unique_value([1, 2, 1, 1]) == 2
    assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
    assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
    assert find_unique_value([6, 6, 6, 6, 6, 6]) == "No unique element found"
    print("ОК")
