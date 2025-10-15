# Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Print a specific student's marks
print("Bob's marks:", students["Bob"])

# Loop through all students and print their names and scores
print("\nAll students:")
for name, marks in students.items():
    print(f"{name}: {marks}")
