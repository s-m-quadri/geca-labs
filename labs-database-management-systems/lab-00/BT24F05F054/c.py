# Task: Create a list of student names (like a table column):
#  - At least 5 student names
#  - Print each name using a for loop
#  - Print total count of students

# 💡 TIP:
# Lists: students = ["Alice", "Bob", ...]
# Loop: for student in students:
# Count: len(students)


students = ["Mayur", "talvinder", "amman", "mangesh"]

n=1
for i in (students):
    print(f"{n}. {i}")
    n+=1

print("total no. of students: ",len(students))