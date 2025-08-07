# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

# Ask user for rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Nested loops to print the rectangle
for i in range(rows):
    for j in range(cols):
        print("*", end="")  # Print asterisk without newline
    print()  # Newline after each row
