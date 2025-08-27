
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Bob's marks:", student_marks["Bob"])

print("---")


for name, marks in student_marks.items():
    print(f"{name}: {marks}")
