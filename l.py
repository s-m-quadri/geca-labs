# Creating a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Bob's marks:", students["Bob"])

# Looping through all students and printing their names and scores
print("\nAll students and their marks:")
for name, marks in students.items():
    print(name, ":", marks)
