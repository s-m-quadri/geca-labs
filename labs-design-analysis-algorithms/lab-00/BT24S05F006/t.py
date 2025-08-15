# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.

# Write 3 lines into the file
with open("output.txt", "w") as f:
    f.write("Line 1: Hello, world!\n")
    f.write("Line 2: This is Python.\n")
    f.write("Line 3: File handling example.\n")

# Read and print the file content
with open("output.txt", "r") as f:
    content = f.read()
    print("File Content:\n" + content)
