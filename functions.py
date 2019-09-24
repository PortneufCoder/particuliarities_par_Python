students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


# assume student_id param has value of 123 if
# nothing else is passed for it function call.


def add_student(name, student_id=123):
    student = {"name": name, "student_id": student_id}
    students.append(student)


student_list = get_students_titlecase()

add_student(name="Victor", student_id=10)


# Setting an unknown number of arguments *args


def var_arguments(name, *args):
    print(name)
    print(args)


var_arguments("Esmerelda", "Loves Python", 123, None, False)

# Using kwargs to add params with a key


def kwargs_test(country, **kwargs):
    print(country)
    print(kwargs["temp"], kwargs["aliens_present"])  # prints the params with those keys


kwargs_test("Pluto", description="Solar System", temp="cold", aliens_present="maybe")
