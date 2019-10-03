from python_OOP.classes import *


class HighSchoolStudent(Student):  # this subclass(derived) can access all methods and vars in parent
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This student attends High School"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()  # super gets the method from the parent
        return original_value + "-HS"



