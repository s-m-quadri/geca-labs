# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

x = int(input("Enter number of rows: "))
y = int(input("Enter number of columns: "))

for i in range(x):
    for j in range(y):
        print("*", end="")
    print()

