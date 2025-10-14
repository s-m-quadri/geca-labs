# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"{num1} divided by {num2} is {result}")
except ValueError:
    print("Error: Please enter valid numbers")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
