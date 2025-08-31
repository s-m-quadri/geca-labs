# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`
def student_info(name, marks):
    print(f"Student {name} scored {marks} marks.")
    print("Student {} scored {} marks.".format(name, marks))
    print("Student %s scored %s marks." % (name, marks))        
student_info("Alice", 92)   
student_info("Bob", 85)

student_info("Charlie", 78)
student_info("Diana", 88)   
student_info("Eve", 95)
student_info("Frank", 80)
             
