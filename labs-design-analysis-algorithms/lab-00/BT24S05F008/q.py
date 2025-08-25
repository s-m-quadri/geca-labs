# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

row = int(input("Enter Number of Rows: "))
col = int(input("Enter Number of Columns: "))

for i in range(0,row):
    for i in range(0,col):
        print("*",end=" ")
    print()