# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
#code
students = {
    "Arjun": 85,
    "Ved": 92,
    "Sid": 78
}

print(f"Arjun's marks: {students['Arjun']}")

for name, marks in students.items():
    print(f"{name}: {marks}")