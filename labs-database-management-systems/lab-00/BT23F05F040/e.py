# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")

def student_name(id, name, age, dept):
    print(f"student detail, \nid\t: {id} \nname\t: {name} \nage\t: {age} \ndept\t: {dept}")
    print("\n")

student_name(1, "Mayur", 20, "CSE")
student_name(2, "Rohan", 19, "CSE")
student_name(3, "Pawan", 21, "CSE")

