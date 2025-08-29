# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
try:
	num1 = float(input("Enter first number: "))
	op = input("Enter operator (+, -, *, /): ")
	num2 = float(input("Enter second number: "))
	if op == '+':
		print("Result:", num1 + num2)
	elif op == '-':
		print("Result:", num1 - num2)
	elif op == '*':
		print("Result:", num1 * num2)
	elif op == '/':
		if num2 != 0:
			print("Result:", num1 / num2)
		else:
			print("Cannot divide by zero.")
	else:
		print("Invalid operator.")
except ValueError:
	print("Invalid input.")
