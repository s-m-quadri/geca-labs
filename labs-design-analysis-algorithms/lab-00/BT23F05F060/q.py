# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.

rows=int(input())
cols=int(input())


for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()