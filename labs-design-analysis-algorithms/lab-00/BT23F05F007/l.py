# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {
    "shrute": 85,
    "amru": 90,
    "bhagya": 78
}

print("amru's marks:", students["amru"])

for name, marks in students.items():
    print(f"{name}: {marks}")