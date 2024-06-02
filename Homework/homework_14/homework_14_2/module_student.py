from module_human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, record#: {self.record_book}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))
