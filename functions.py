students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


# assume student_id param has value of 123 if
# nothing else is passed for it in function call.


def add_student(name, student_id=123):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except OSError or IOError as error:
        print("Could not save the file")
        print(error)


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
            f.close()
    except OSError or IOError as error:
        print("Could not read file")
        print(error)


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)


# Setting an unknown number of arguments *args


def var_arguments(name, *args):
    print(name)
    print(args)


var_arguments("Esmerelda", "Loves Python", 123, None, False)


# Using kwargs to add params with a key


def kwargs_test(country, **kwargs):
    print(country)
    print(kwargs["temp"], kwargs["aliens_present"])  # prints the values with those keys


kwargs_test("Pluto", description="Solar System", temp="cold", aliens_present="maybe")


def banner(message, border="^"):
    """when passing default args, it must be added
    after non-default args or else we get a syntax error"""

    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Irish Cream")
banner("The Grass is Singing", "-")  # run time arg replaces default arg
