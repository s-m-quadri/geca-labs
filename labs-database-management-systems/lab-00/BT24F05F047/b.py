# Task: Create variables for a student record:
#  - student_id (integer, e.g., 101)
#  - student_name (string, e.g., "Alice")
#  - marks (float, e.g., 85.5)
#  - department (string, e.g., "CSE")
# Print all variables in a formatted way.

# 💡 TIP:
# Use f-strings for formatting: f"ID: {student_id}"

student_id = 101
student_name = "Alice"
marks = 85.5
department = "CSE"

def main() -> None:
	print(f"ID: {student_id}")
	print(f"Name: {student_name}")
	print(f"Marks: {marks:.1f}")
	print(f"Department: {department}")


if __name__ == "__main__":
	main()


