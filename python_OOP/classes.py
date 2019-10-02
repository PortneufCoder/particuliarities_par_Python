students = []


class Student:
    def add_student(self, name, student_id=123):  # self == this in JS
        student = {"name": name, "student_id": student_id}
        students.append(student)


