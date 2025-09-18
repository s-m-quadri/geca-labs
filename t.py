# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
# Writing to the file
with open("output.txt", "w") as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

# Reading from the file
with open("output.txt", "r") as f:
    content = f.read()

# Printing the content
print("File content:\n", content)
