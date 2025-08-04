# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows=int(input("enter height"))
column=int(input("enter width"))
for i in  range(rows):
    for j in range (column):
        print("*",end="");
    print()
