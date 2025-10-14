# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {
    "Ankit": 85,
    "Riya": 92,
    "Samar": 78
}

print(students["Riya"])

for name, marks in students.items():
    print(name, marks)
