class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self) -> int:
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        result_add = self.get_square() + other.get_square()
        width_add = self.width
        height_add = result_add // width_add
        return Rectangle(width_add, height_add)

    def __mul__(self, n):
        result_mul = self.get_square() * n
        height_mul = self.height
        width_mul = result_mul // height_mul
        return Rectangle(width_mul, height_mul)

    def __str__(self):
        return f"The square is {self.get_square()}. The width of the rectangle is {self.width}, the height is {self.height}."


if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)

    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    assert r3.get_square() == 26, 'Test3'

    r4 = r1 * 4
    assert r4.get_square() == 32, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

    print(r1.get_square())
    print(r2.get_square())
    print(r1.__eq__(r2))
    print(r1.__add__(r2))
    print(r1.__mul__(4))
    print(r4.__str__())
