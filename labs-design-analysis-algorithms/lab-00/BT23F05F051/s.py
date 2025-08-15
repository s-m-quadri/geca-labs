# Take two numbers from the user and divide them.
#  - Handle divide-by-zero errors using try-except.
#  - Also handle non-integer input using `try` and `ValueError`.

# 💡 TIP:
# Use `except ZeroDivisionError:` and `except ValueError:` blocks.


try:
    a=int(input())
    b=int(input())
    result=a/b
    print(result)
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("enter valid numbers")
