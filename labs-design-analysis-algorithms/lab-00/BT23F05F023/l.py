# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
my_dict = {'John': 85, 'Alice': 92, 'Bob': 78}
print("Alice's marks:", my_dict['Alice'])
for name, marks in my_dict.items():   
    print(f"Student: {name}, Marks: {marks}")           
    