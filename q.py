# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns "))

for i in range(row):
    for j in range(column):
        print("*", end = "")
    print()    