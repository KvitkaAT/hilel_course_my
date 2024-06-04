from student import Student

from group import Group

from exception import LimitReachedError


if __name__ == '__main__':
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

    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)  # Only one student
