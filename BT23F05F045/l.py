# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {"A": 55, "B": 97, "C": 84}

print("B Marks:", students["B"])

for name, marks in students.items():
    print(f"{name} scored {marks}")

