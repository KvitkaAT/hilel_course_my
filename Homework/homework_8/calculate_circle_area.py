import math


def calculate_circle_area(radius: int) -> float:
    circle_area = 3.14 * radius ** 2
    return circle_area


if __name__ == "__main__":
    assert calculate_circle_area(5), (rel_tol=1e-2) == 78.5
    assert calculate_circle_area(0) == 0
    assert calculate_circle_area(10) == 314.2
