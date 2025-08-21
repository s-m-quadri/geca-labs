# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.

file = open("output.txt","w")
file.write("Hello,Bharti\n")
file.write("How are you?\n")
file.write("Welcome to github codespaces")


with open("output.txt", "r") as file:
    content = file.read()

print(content)