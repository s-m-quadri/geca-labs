# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
for row in range(0,rows):
    for col in range(0,columns):
        print("*",end="")
    print()