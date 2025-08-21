# Create a file named `output.txt`, write 3 lines into it, then read and print the content.
#  - Use file modes `'w'` and `'r'`.

# 💡 TIP:
# Use `with open(...) as f:` to auto-close files.
def file_write_read():
   
    with open("output.txt", "w") as f:
        f.write("Line 1: Hello, this is the first line.\n")
        f.write("Line 2: Writing to a file in Python.\n")
        f.write("Line 3: Now we will read it back.\n")
    
  
    with open("output.txt", "r") as f:
        content = f.read()
    

    print("File content:\n")
    print(content)


file_write_read()
