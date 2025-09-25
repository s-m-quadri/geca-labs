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
# Recursive function
def print_reverse_recursive(arr, index=None):
    if index is None:  # initialize index on first call
        index = len(arr) - 1
    if index < 0:  # base case
        return
    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)

# Iterative function
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")

# -------------------------------------------
# Example Usage
arr = [1, 2, 3, 4]

print("Recursive Output:")
print_reverse_recursive(arr)

print("\nIterative Output:")
print_reverse_iterative(arr)