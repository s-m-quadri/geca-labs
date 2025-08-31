# -------------------------------------------
# TASK: Print Elements of Array in Reverse
# -------------------------------------------
# Write two functions:
#   1. print_reverse_recursive(arr): prints last to first using recursion
#   2. print_reverse_iterative(arr): prints using a loop
#
# Example:
#   Input: [1, 2, 3, 4]
#   Output: 4 3 2 1
#
# -------------------------------------------
# HINTS:
# - For recursion, start from last index: len(arr) - 1
# - Reduce index by 1 each call
# - For iteration, use a loop from end to start

def print_reverse_recursive(a, n):
    if n == 0:
        return
    print(a[n-1], end=" ")
    print_reverse_recursive(a, n-1)

def print_reverse_iterative(a):
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=" ")

arr = [1,6,2,3,4,5,3]
print_reverse_recursive(arr, len(arr))
print()
print_reverse_iterative(arr)
