
students = {"Alice": 92, "Bob": 85, "Charlie": 78}
print("Alice's marks:", students["Alice"])
for name, marks in students.items():
	print(f"{name}: {marks}")
# Use dict[key] to access values, and `.items()` to loop.
