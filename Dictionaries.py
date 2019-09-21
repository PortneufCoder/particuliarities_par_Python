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
