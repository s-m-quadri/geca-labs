# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.

with open("output.txt","w") as file:
    file.write("My name is Akshay\n")
    file.write("I am a student\n")
    file.write("Completing DAA Lab\n")

with open("output.txt", "r") as file:
    data = file.read()
    print(data)