# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

student = {
    "Akshay" : 90,
    "Rohan" : 80,
    "Amit" : 75
}

for key,value in student.items():
    print(f"{key} : {value}")