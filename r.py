# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`

def student_info(name, marks):
    print(f"Student {name} scored {marks} marks.")   # Using f-string
    print("Student {} scored {} marks.".format(name, marks))  # Using format()
    print("Student %s scored %s marks." % (name, marks))      # Using %s

student_info("Alice", 92)

