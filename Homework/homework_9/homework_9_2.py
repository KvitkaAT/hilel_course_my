def difference(*args: int | float) -> int | float:
    if len(args) == 0:  # if no arguments, return 0
        return 0
    return max(args) - min(args)  # calculates the difference between the max amd min argument


if __name__ == "__main__":
    assert difference(1, 2, 3) == 2
    assert difference(5, -5) == 10
    assert round(difference(10.2, -2.2, 0, 1.1, 0.5), 2) == 12.4
    assert difference() == 0
    print('OK')
