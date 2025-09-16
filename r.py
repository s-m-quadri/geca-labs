# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`
# Using f-strings
def student_info(name, marks):
    print(f"Student {name} scored {marks} marks.")

# Testing the function
student_info("Alice", 92)

# Using .format()
print("Student {} scored {} marks.".format("Bob", 85))

# Using % formatting
print("Student %s scored %d marks." % ("Charlie", 78))
