# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

# Ask user for number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Print the rectangle using nested loops
for i in range(rows):             # outer loop → rows
    for j in range(cols):         # inner loop → columns
        print("*", end="")        # print * without newline
    print()                       # move to next line after each row
