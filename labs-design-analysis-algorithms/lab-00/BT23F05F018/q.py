# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


for _ in range(rows):          # Outer loop for rows
    for _ in range(cols):      # Inner loop for columns
        print("*", end="")     # Print without newline
    print()                    # Move to next row
