from exception import LimitReachedError

from student import Student


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
