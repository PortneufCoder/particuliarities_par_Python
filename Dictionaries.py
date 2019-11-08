student = {
    "name": "Vince",
    "student_id": 15163,
    "feedback": None
}

all_students = [
    {"name": "Shonda", "student_id": 12369},
    {"name": "Katia", "student_id": 45302}
]

for student in all_students:
    if student["name"] == "Shonda":
        print(student["student_id"])

print(student.keys())
print(student.values())

cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

print(dir(cast))
#  If you wish to iterate through both keys and values, you can use the built-in method items() like this:
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for stuff, value in basket_items.items():
    if stuff in fruits:
        result += value
# if the key is in the list of fruits, add the value (number of fruits) to result


print(result)

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
print(dir(fruits))
# Iterate through the dictionary
for fruit, number in basket_items.items():
    if fruit in fruits:
        fruit_count += number
    if fruit not in fruits:
        not_fruit_count += number

print("The number of fruits is {}. There are {} objects that are not fruits".format(fruit_count, not_fruit_count))

new_list = []
total_odds = 5

for number in num_list:
    if number / 2 == 0:
        new_list.append(number)
    if len(new_list) == total_odds:
        break


print(new_list)
