# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

students = {
    "A": 85,
    "B": 90,
    "C": 78
}

print("B's marks:", students["B"])

for name, marks in students.items():
    print(f"{name}: {marks}")