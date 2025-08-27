# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
with open("output.txt","w") as f:
    f.write("hello\n")
    f.write("hii\n")
    f.write("bye")
with open("output.txt","r") as f:
    data=f.read()
print(data)