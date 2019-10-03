students = []


class Student:
    school_name = "Springfield Elementary"  # can be called directly since its a class attribute ! an instance attribute

    def __init__(self, name, student_id=123):  # self == this in JS
        self.name = name
        self.student_id = student_id
        students.append(self)  # append all attributes to list

    def __str__(self):  # this method overrides the first method
        return "Student's name is " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


homer = Student("Homer")  # class initialization


class HighSchoolStudent(Student):  # this subclass(derived) can access all methods and vars in parent
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This student attends High School"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()  # super gets the method from the parent
        return original_value + "-HS"


bart = HighSchoolStudent("bart")
print(bart.get_name_capitalized())
