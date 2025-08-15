# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
dict1={"Aditya":99, "Aryan":98,"ronit":89}
print(dict1["Aditya"])
for name,marks in dict1.items():
    print(f"name:{name} ,marks:{marks}")