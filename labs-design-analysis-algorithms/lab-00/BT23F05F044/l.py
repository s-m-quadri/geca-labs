# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {"shrutee": 97, "sakshi": 92, "mayuri": 94}
print(students["sakshi"])
for name, marks in students.items():
    print(name, marks)
