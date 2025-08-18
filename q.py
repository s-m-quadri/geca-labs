# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows = float(input("Enter number of rows: "))
cols = float(input("Enter number of columns: "))

for i in range(int(rows)):
    for j in range(int(cols)):
        print("*", end="")
    print() 
