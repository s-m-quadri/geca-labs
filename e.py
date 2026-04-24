# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")

def display_student(name, age, dept):
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"Department : {dept}")
    print("-" * 25)

display_student("Rahul", 20, "CSE")
display_student("Sneha", 19, "IT")
display_student("Amit", 21, "Mechanical")
