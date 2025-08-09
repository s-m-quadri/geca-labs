# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

Student = {
    "Riya": 98,
    "Megha": 85,
    "Nayan": 70
}
print("Riya's Marks: ", Student["Riya"])
for name, marks in Student.items():
    print(name, " : ", marks)