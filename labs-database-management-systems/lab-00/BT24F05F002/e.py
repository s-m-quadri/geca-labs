# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")

def display_student(name, age, dept):
    print(f"Student name : {name}")
    print(f"Student age : {age}")
    print(f"Student department: {dept}")

# calling function with 3 different names
display_student("aditya", 20, "CSE")
display_student("ali", 19, "MECH")
display_student("harpreet", 25, "CSE")
