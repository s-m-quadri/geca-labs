# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.


try:
    # Take input from user
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))

    # Perform division
    result = x / y
    print("Result:", result)

# Handle divide by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handle invalid input
except ValueError:
    print("Error: Please enter valid integers!")
