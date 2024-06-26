class Rectangle:
    def __init__(self, height, width):
        self.hight = height
        self.width = width

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


square = Square(5)
assert square.calculate_area() == 25
