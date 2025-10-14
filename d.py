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
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
power = num1 ** num2

# Print the results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)
print("Power:", power)
