# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows=int(input("Rows: "))
cols=int(input("Columns: "))
for _ in range(1,rows+1):
    for _ in range(cols+1):
        print(" *",end="")
    print()