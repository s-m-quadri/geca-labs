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
# Program to perform arithmetic operations on two numbers

# Taking input from the user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Performing operations
print("\nResults:")
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)

# Checking for division by zero
if y != 0:
    print("Quotient:", x / y)
    print("Remainder:", x % y)
else:
    print("Quotient: Undefined (division by zero)")
    print("Remainder: Undefined (division by zero)")

print("Power (x^y):", x ** y)

