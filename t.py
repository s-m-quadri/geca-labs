with open("output.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
with open("output.txt", "r") as f:
    print(f.read())
