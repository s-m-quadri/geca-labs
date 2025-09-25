# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.

directory={
    "one":1,
    "two":2,
    "three":3
}

print(directory["one"])
for key,value in directory.items():
    print(key,value)

