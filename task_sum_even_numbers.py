# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------
# Write two functions:
#   1. sum_even_recursive(n): uses recursion
#   2. sum_even_iterative(n): uses a loop
#
# Example:
#   Input: n = 10
#   Output: 2 + 4 + 6 + 8 + 10 = 30
#
# -------------------------------------------
# HINTS:
# - Base case for recursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version

def sum_even_iterative(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 ==0:
            sum +=i
    return sum

def sum_even_recursive(n,sum):
    if n == 0:
        return sum
    if n%2 == 0:
        sum += n
    return sum_even_recursive(n-1,sum)

print("Sum Iteratively : ",sum_even_iterative(10))
print("Sum Recursively : ",sum_even_recursive(10,0))
