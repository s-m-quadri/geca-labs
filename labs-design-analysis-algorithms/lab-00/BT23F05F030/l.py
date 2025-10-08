# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
students = {
    "Gargee" : 99,
    "Nandini" : 98,
    "Prajakta" : 97
}

print("Gargee's marks:", students["Gargee"])

for name, marks in students.items():
    print(f"{name}: {marks}")