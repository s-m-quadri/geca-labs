# Task: Create a list of student names (like a table column):
#  - At least 5 student names
#  - Print each name using a for loop
#  - Print total count of students

# 💡 TIP:
# Lists: students = ["Alice", "Bob", ...]
# Loop: for student in students:
# Count: len(students)

student_list = ["aditya", "ram", "ali", "harpreet", "steve", "isaac", "tenzin"]

count = 0
for n in student_list:
    print(f"name : {n}")
    count += 1

# counting names by loop
print(f"the total number student are {count}")

# counting names by build in method
print(f"the total number student are {len(student_list)}")
