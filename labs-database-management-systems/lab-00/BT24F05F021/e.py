# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")

def display_student(name, age, dept):
    print("Student Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {dept}")
    print("----------------------")

display_student("Mayuri", 20, "CSE")
display_student("Atharv", 21, "IT")
display_student("Jyoti", 19, "ECE")
