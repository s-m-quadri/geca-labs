# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {
    "Ben": 85,
    "Ollie": 92,
    "Joe": 78
}

print("Joe's marks:", students["Joe"])

for name, marks in students.items():
    print(f"{name}: {marks}")
