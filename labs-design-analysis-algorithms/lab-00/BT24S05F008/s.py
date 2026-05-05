# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

try:
    print(a//b)
except:
    print("ZeroDivisonError")
