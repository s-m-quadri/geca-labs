# Task: Write a function to display student information:
#  - Function name: display_student(name, age, dept)
#  - It should print the details in a formatted way
#  - Call this function 3 times with different students

# 💡 TIP:
# def function_name(param1, param2):
#     print(f"Student: {param1}")


# Defining the function
def display_student(name, age, dept):
    print(f"Name: {name}, Age: {age}, Department: {dept}")

# Calling the function with different students
display_student("Alice", 20, "CSE")
display_student("Bob", 21, "IT")
display_student("Charlie", 19, "ECE")