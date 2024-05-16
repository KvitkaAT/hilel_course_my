def difference(*args: int | float) -> int | float:
    if len(args) == 0:  # if no arguments, return 0
        return 0
    return round(max(args) - min(args), 2)  # calculates the difference between the max amd min argument
#  rounds a result to 2 digits after the decimal point


if __name__ == "__main__":
    assert difference(1, 2, 3) == 2
    assert difference(5, -5) == 10
    assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    assert difference() == 0
    print('OK')
