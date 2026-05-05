def student_info(name, marks):
    
    print(f"Student {name} scored {marks} marks.")

    
    print("Student {} scored {} marks.".format(name, marks))

    
    print("Student %s scored %s marks." % (name, marks))


student_info("Alice", 92)
