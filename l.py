# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

# Create a dictionary with 3 student names and their marks
students = {
    "Rama": 92,
    "Aarav": 85,
    "Isha": 78
}

# Print a specific student's marks
print("Rama's marks:", students["Rama"])

# Loop through all students and print their names and scores
print("\nAll students and their marks:")
for name, marks in students.items():
    print(name, ":", marks)
