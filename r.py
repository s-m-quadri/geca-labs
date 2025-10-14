# Using f-strings
def student_info_fstring(name, marks):
    print(f"Student {name} scored {marks} marks.")

# Using .format()
def student_info_format(name, marks):
    print("Student {} scored {} marks.".format(name, marks))

# Using % formatting
def student_info_percent(name, marks):
    print("Student %s scored %s marks." % (name, marks))

# Calling the functions
student_info_fstring("Alice", 92)
student_info_format("Bob", 85)
student_info_percent("Charlie", 78)
