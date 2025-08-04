# Print a rectangle made of asterisks `*` of size rows × cols.
#  - Ask user for number of rows and columns.
#  - Use nested loops.

# 💡 TIP:
# Outer loop → rows; Inner loop → columns.
r=int(input("enter row:"))
c=int(input("enter columns:"))
for i in range(0,r):
    for j in range(0,c):
        print("*" ,end="")
    print(" ")