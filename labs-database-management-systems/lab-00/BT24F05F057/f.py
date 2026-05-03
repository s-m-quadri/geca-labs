# Task: Write student data to a file (simulating data persistence):
#  - Create a file named "students.txt"
#  - Write at least 3 student records (one per line)
#  - Format: Name,Age,Department
#  - Then read and print the file contents

# 💡 TIP:
# Write: with open("file.txt", "w") as f:
#           f.write("text\n")
# Read: with open("file.txt", "r") as f:
#          print(f.read())


# Writing to student.txt 
for i in range(3):
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    dept  = input("Enter Department Name : ")
    print("-"*50)
    with open("students.txt","a") as f:
        f.write("="*60)
        f.write(f"\nStudent Record : {i+1}\nName: {name}\nAge:{age}\nDepartment:{dept}\n")
        f.write("="*60)

# Reading from File
print("-------- Reading From File students.txt ---------")
with open("students.txt",'r') as f:
    print(f.read())
    

