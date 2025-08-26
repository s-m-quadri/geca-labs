# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

dic={"A":85,"B":78,"C":89}
print(f"C: {dic["C"]}")
print(dic.items())
for i in list(dic.items()):
    print(i)