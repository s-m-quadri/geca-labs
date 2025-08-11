# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
Students={"Radha":75,"vikram":80,"Anil":90}
print("Vikram's marks: ",Students["vikram"])
for names,marks in Students.items():
    print(names, ":", marks)