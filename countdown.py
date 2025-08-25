# -------------------------------------------
# Problem: Print numbers from n to 1
# -------------------------------------------
# Goal: Practice recursion vs iteration
# -------------------------------------------

# Recursive version
def countdown_recursive(n):
    if n == 0:
        return
    print(n)
    countdown_recursive(n - 1)

# Iterative version
def countdown_iterative(n):
    while n > 0:
        print(n)
        n -= 1

# Try both
n = 5
print("Recursive countdown:")
countdown_recursive(n)

print("\nIterative countdown:")
countdown_iterative(n)
#  Completed the program