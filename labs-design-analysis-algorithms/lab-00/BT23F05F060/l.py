# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

students = {
    "Aryan": 100,
    "Adi": 90,
    "Om": 78
}

print("Adi's marks:", students["Adi"])

for name, marks in students.items():
    print(f"{name}: {marks}")