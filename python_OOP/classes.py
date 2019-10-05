students = []


class Student:
    school_name = "Springfield Elementary"  # can be called directly since its a class attribute ! an instance attribute

    def __init__(self, name, last_name, student_id=123):  # self == this in JS
        self.name = name
        self.student_id = student_id
        self.last_name = last_name
        students.append(self)  # append all attributes to list

    def __str__(self):  # this method overrides the first method
        return "Student's name is " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


#  homer = Student("Homer")  # class initialization


