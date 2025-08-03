# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = x / y
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
