# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`
def student_info(name,marks):
    print(f"Student {name} second {marks} marks.")
    print("Student {} second {} marks." .format(name, marks))
    print("Student %s scored %s marks. " %(name,marks))

student_info("Prajakta", 98)    