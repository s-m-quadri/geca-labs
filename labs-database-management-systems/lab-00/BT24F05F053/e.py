# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")
def display_student(name, age, dept):
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Department: {dept}")
    print("-" * 30)

display_student("Alice", 20, "Computer Science")
display_student("Bob", 21, "Electrical Engineering")
display_student("Charlie", 19, "Mechanical Engineering")

