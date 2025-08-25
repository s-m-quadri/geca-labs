# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
marks={
    "Aryan":65,
    "bhargav":73,
    "cherith":90,
}
for name, marks in marks.items():
    print(f"{name} scored{marks}marks.")