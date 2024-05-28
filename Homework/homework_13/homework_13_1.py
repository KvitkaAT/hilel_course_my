class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self. last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, record#: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        for student in self.group:  # iterates through all students in a group
            if student.last_name == last_name:  # finds a student by the last name
                self.group.discard(student)  # deletes a student instance from a group (set)
                break  # if student was found, breaks the loop

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:  # iterates through all students in a group
            if student.last_name == last_name:  # finds a student by the last name
                return student  # returns the student instance
        return None  # if a student was not found, return None

    def __str__(self) -> str:
        all_students = "\n".join(str(student) for student in self.group)  # adds a student instance to a string
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)


if __name__ == "__main__":
    assert str(gr.find_student('Jobs')) == str(st1)
    assert gr.find_student('Jobs2') is None
    assert isinstance(gr.find_student('Jobs'), Student) is True

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
