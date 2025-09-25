
with open('output.txt', 'w') as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: This is a test.\n")
    f.write("Line 3: Goodbye!\n")


with open('output.txt', 'r') as f:
    content = f.read()
    print(content)
