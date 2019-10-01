students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students():
            students.append(student)
            f.close()
    except OSError or IOError as error:
        print("Could not read file")
        print(error)


def read_students(f):
    for line in f:
        yield line  # return each line from the student list


read_file()
print(students)