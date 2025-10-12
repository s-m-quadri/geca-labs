# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
# Create a dictionary with 3 Indian student names and their marks
student_marks = {
    "Aarav": 85,
    "Isha": 92,
    "Rahul": 78
}

# Print a specific student's marks
print("Isha's marks:", student_marks["Isha"])

# Loop through all students and print their names and scores
for name, marks in student_marks.items():
    print(f"{name}: {marks}")
