# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

students = {"Raj": 85, "Ram": 90, "Teja": 78}

print(students["Ram"])

for name, marks in students.items():
    print(f"{name}: {marks}")
