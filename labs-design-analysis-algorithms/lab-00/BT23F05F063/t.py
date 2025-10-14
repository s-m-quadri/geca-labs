# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.

# Writing to the file
with open('output.txt', 'w') as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python is fun\n")
    f.write("Line 3: File handling demo\n")

# Reading from the file
print("File contents:")
with open('output.txt', 'r') as f:
    print(f.read())
