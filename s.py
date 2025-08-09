# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid numbers")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
