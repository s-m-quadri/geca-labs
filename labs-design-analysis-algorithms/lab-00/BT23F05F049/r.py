# Write a function `student_info(name, marks)` that prints:
#  "Student Alice scored 92 marks." using f-strings.
#  Try the same with `.format()` and `%s`.

# 💡 TIP:
# Use `f"{name} scored {marks}"` or `"{} scored {}".format(...)`
def student_info(name, marks):
    print(f"{name} scored {marks} marks")
    # By using .format()
    print("{} scored {} marks".format(name,marks))
    # By using %s and %d
    print("%s scored %d marks." % (name, marks))

# Driver code
student_info("Janvi",90)