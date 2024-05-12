import math


def find_gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


if __name__ == "__main__":
    assert find_gcd(12, 18) == 6
    assert find_gcd(15, 25) == 5
    assert find_gcd(7, 11) == 1
    assert find_gcd(30, 45) == 15
    assert find_gcd(17, 23) == 1
    print("Ok")





