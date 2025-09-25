# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    Division=a/b
except ZeroDivisionError:
    print("Can't divided by zero")

except ValueError:
    print("Enter integer value only")
