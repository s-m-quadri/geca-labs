# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    div = num1/num2
    print(f"Result : {div}")

except ZeroDivisionError:
    print("Error : Cannot divide by Zero")

except ValueError:
    print("Error : Please enter valid integer")