

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))


sum_result = x + y
difference = x - y
product = x * y


if y != 0:
    quotient = x / y
    remainder = x % y
else:
    quotient = "undefined (division by zero)"
    remainder = "undefined (modulo by zero)"

power = x ** y


print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print(f"Power (x^y): {power}")

