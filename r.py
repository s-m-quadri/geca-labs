# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`

def student_info_f(name, marks):
    print(f"Student {name} scored {marks} marks.")

def student_info_format(name, marks):
    print("Student {} scored {} marks.".format(name, marks))

def student_info_percent(name, marks):
    print("Student %s scored %s marks." % (name, marks))

student_info_f("Alice", 92)
student_info_format("Alice", 92)
student_info_percent("Alice", 92)
