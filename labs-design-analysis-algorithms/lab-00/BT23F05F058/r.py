def student_info(name, marks):
    # Using f-string
    print(f"Student {name} scored {marks} marks.")
    
    # Using str.format()
    print("Student {} scored {} marks.".format(name, marks))
    
    # Using % formatting
    print("Student %s scored %d marks." % (name, marks))

# Example usage
student_info("Alice", 92)
