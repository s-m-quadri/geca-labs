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
# Function 1: Recursion
def print_reverse_recursive(arr, index=None):
    # Set index to last element on first call
    if index is None:
        index = len(arr) - 1
    
    # Base case: stop when index is less than 0
    if index < 0:
        return
    
    # Print current element
    print(arr[index], end=" ")
    
    # Recursive call for previous index
    print_reverse_recursive(arr, index - 1)


# Function 2: Iteration
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):  # from last to first
        print(arr[i], end=" ")


# ----------------------------
# Example usage
arr = [1, 2, 3, 4]
print("Recursive Output:")
print_reverse_recursive(arr)

print("\nIterative Output:")
print_reverse_iterative(arr)
