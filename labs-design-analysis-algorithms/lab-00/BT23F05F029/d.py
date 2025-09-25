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

# Take two numbers from the user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Perform operations
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)       # division
print("Remainder:", x % y)      # modulus
print("Power:", x ** y)         # x raised to the power y
