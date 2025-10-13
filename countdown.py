# -------------------------------------------
# Problem: Print numbers from n to 1
# -------------------------------------------
# Goal: Practice recursion vs iteration
# -------------------------------------------

# Recursive version
def fun(n):
    if n == 0:    # base case
        return
    print(n)
    fun(n-1)      # recursive call

# Iterative version
def fun2(n):
    while n >= 1:
        print(n)
        n -= 1

# Try both
n = 10
print("Recursive countdown:")
fun(n)

print("\nIterative countdown:")
fun2(n)
