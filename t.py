# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.

with open('output.txt', 'w') as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print("File 'output.txt' has been created and written to.")

with open('output.txt', 'r') as f:
    content = f.read()
    print("\nContent of output.txt:")
    print(content)