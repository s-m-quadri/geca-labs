# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

# Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Print a specific student's marks
print("Bob's marks:", students["Bob"])

# Loop through all students and print their names and scores
print("\nAll students and their marks:")
for name, marks in students.items():
    print(name, ":", marks)
