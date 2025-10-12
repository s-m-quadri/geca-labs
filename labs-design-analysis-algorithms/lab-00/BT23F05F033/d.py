# Write a program that takes two numbers from the user.
# Print their:
#  - sum
#  - difference
#  - product
#  - quotient
#  - remainder
#  - power (x^y)

# 💡 TIP:
# Use `+`, `-`, `*`, `/`, `%`, and `**`.
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

print("Sum : ", x+y)
print("Difference : ",x-y)
print("Product : ",x*y)

if y!= 0:
    print("Quotient : ",x/y)
    print("Remainder : ",x%y)
else: 
    print("Quotinent: Undefined (division by zero)")    
    print("Remainder: Undefined (division by zero)") 

print("Power (x^y):", x**y)