# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print(f"Alice's marks: {students['Alice']}")

print("\nAll students and their scores:")
for name, score in students.items():
    print(f"{name}: {score}")