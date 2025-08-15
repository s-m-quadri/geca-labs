# Create a dictionary with 3 student names and their marks.
# Print a specific student's marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

students = {"Siya": 92, "Ayan": 78, "Sulabh": 85}
print("Siya's marks:", students["Siya"])

print("All students:")
for name, marks in students.items():
    print(f"{name}: {marks}")
