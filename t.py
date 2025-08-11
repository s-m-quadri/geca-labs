# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
with open("output.txt", "w") as f:
    f.write("HI\nGoogle\nby\n")
with open("output.txt", "r") as f:
    print(f.read())