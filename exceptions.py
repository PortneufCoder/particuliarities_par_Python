student = {"name": "Vince", "student_id": 15163, "feedback": None, "last_name": "Bart"}

try:
    last_name = student["last_name"]
    last_name_number = 5 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add an int and str!")
    print(error)

print("This code executed!")

# KeyError(No last_name key)


