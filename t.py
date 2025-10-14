# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("output.txt", "w") as f:
    f.writelines(lines)

with open("output.txt", "r") as f:
    content = f.read()

print(content)
