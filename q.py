# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows = int(input("Rows: "))
cols = int(input("Columns: "))
for r in range(rows):
    for c in range(cols):
        print("*", end="")
    print()
