# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")


def display_student(name:str, age:int, dept:str):
    """ To Display Student Information """
    print(f"Student Name : {name}")
    print(f"Student Age : {age}")
    print(f"Student Department : {dept}")
    print("-"*80)

display_student("Adarsh",21,"CSE")
display_student("Serena",16,"ELE")
display_student("Ash",19,"IT")


