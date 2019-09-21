# Working with lists
student_names = ["Jake", "Thomas", "Sebastien", "Katarina", "Mark", "Frank Grimes"]

# Automatic detection of full list
for name in student_names:
    print("Student name is {0}".format(name).capitalize())

# Use range to set the amount of times loop runs

a = 0
for index in range(10):
    a += 15
    print("The value of A is {0}".format(a))

for name in student_names:
    if name == "Katarina":
        print("Found her! " + name)
        break
    print("Currently testing " + name)

for name in student_names:
    if name == "Frank Grimes":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)