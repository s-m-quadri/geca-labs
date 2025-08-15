# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {
    "Raaj": 45,
    "Rahul": 36,
    "Ram": 50
}

print("Rahul's's marks:", students["Rahul"])

for name, marks in students.items():
    print(f"{name}: {marks}")