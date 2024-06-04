class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, record#: {self.record_book}"


class LimitReachedError(Exception):
    pass


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise LimitReachedError(f"The student {student} can not be added. Too many students in a group.")
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        for student in self.group:  # iterates through all students in a group
            if student.last_name == last_name:  # finds a student by the last name
                self.group.discard(student)  # deletes a student instance from a group (set)
                break  # if student was found, breaks the loop

    def find_student(self, last_name: str) -> Student | None:
        return next((student for student in self.group if student.last_name == last_name), None)
        # iterates through all students in a group

    def __str__(self) -> str:
        all_students = "\n".join(str(student) for student in self.group)  # adds a student instance to a string
        return f"Number:{self.number}\n{all_students} "


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 40, 'Anna', 'Green', 'AN146')
st4 = Student('Male', 50, 'Gregory', 'House', 'AN147')
st5 = Student('Male', 42, 'James', 'Wilson', 'AN148')
st6 = Student('Female', 60, 'Hillary', 'Clinton', 'AN149')
st7 = Student('Female', 24, 'Scarlett', 'Ohara', 'AN150')
st8 = Student('Male', 52, 'Barak', 'Obama', 'AN151')
st9 = Student('Female', 29, 'Melissa', 'Stone', 'AN152')
st10 = Student('Male', 37, 'Fernando', 'Rodrigez', 'AN153')
st11 = Student('Female', 39, 'Jessica', 'Alba', 'AN154')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]
gr = Group('PD1')
for student in students[:10]:
    gr.add_student(student)
print(gr)


try:
    gr.add_student(st11)
except LimitReachedError as e:
    print(e)

if __name__ == "__main__":
    assert str(gr.find_student('Jobs')) == str(st1)
    assert gr.find_student('Jobs2') is None
    assert isinstance(gr.find_student('Jobs'), Student) is True

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
