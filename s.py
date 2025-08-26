# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

num1=int(input("Number 1: "))
num2=int(input("Number 2: "))
try:
    print(f"Divition -> {num1}/{num2}={num1/num2}")
except ZeroDivisionError:
    print(f"Divition - {num1}/{num2}=Undefine")
except ValueError:
    print("Invalid Value")