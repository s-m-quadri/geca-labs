# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))

for i in range(a):
    for j in range(b):
        print("*", end="")
    print()
