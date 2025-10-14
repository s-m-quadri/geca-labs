# Asking user for number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Printing the rectangle using nested loops
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()  # Move to the next line after each row
