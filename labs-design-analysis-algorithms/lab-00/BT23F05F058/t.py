# Write to the file
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Read from the file
with open("output.txt", "r") as f:
    content = f.read()

# Print file content
print(content)
