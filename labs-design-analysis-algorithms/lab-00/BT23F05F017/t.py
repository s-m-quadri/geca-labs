# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")


with open("output.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)
