def calculate_square_area(side):
    assert side > 0, AssertionError("Side must be a positive number")
    return side ** 2


area = calculate_square_area(4)
print(area)

area = calculate_square_area(-3)
print(area)
