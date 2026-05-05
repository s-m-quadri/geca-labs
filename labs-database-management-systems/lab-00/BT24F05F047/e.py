# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")


def display_student(name: str, age: int, dept: str) -> None:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {dept}")
    print("-" * 20)
