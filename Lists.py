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
        break  # stop execution of the loop and move to next line
    print("Currently testing " + name)

for name in student_names:
    if name == "Frank Grimes":
        continue  # skip item and go on with the loop
        print("Found him! " + name)
    print("Currently testing " + name)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

user_names = []

for name in names:
    name = name.replace(' ', "_")
    user_names.append(name.lower())

print(user_names)

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print("The numbers of odd numbers added are: {}".format(count_odd))
print("The sum of the odd numbers added is: {}".format(list_sum))
