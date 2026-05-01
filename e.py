# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")

def display_student(name, age, dept):
    """Display formatted student information."""
    print(f"  Name: {name:15} | Age: {age:2} | Department: {dept}")
    return f"{name}_{dept}"

print("\n" + "="*50)
print("STUDENT INFORMATION")
print("="*50)
print("Name           | Age | Department")
print("-"*50)
student1 = display_student("Alice", 20, "CSE")
student2 = display_student("Bob", 21, "ECE")
student3 = display_student("Charlie", 19, "ME")
print("="*50)
print(f"\nStudent IDs: {student1}, {student2}, {student3}")


