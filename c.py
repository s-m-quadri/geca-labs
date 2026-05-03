# Task: Create a list of student names (like a table column):
#  - At least 5 student names
#  - Print each name using a for loop
#  - Print total count of students

# 💡 TIP:
# Lists: students = ["Alice", "Bob", ...]
# Loop: for student in students:
# Count: len(students)

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

print("\n" + "="*40)
print("STUDENT LIST")
print("="*40)
print("Student Names:")
for idx, student in enumerate(students, 1):
    print(f"  {idx}. {student}")

print("\n" + "-"*40)
print(f"Total number of students: {len(students)}")
print(f"Sorted order: {', '.join(sorted(students))}")
print("="*40)


