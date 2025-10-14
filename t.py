# Writing to a file
with open("output.txt", "w") as f:
    f.write("Line 1: Hello Python\n")
    f.write("Line 2: Learning file handling\n")
    f.write("Line 3: Practice makes perfect\n")

# Reading from the file
with open("output.txt", "r") as f:
    content = f.read()

# Printing the file content
print("File content:")
print(content)
