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
# Function to print array elements in reverse using recursion
def print_reverse_recursive(arr, index=None):
    if index is None:
        index = len(arr) - 1  # start from last element
    
    # Base case
    if index < 0:
        return
    
    # Print current element
    print(arr[index], end=" ")
    
    # Recursive call for previous element
    print_reverse_recursive(arr, index - 1)


# Function to print array elements in reverse using iteration
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):  # loop from last to first
        print(arr[i], end=" ")


# -------------------------------
# Example usage:
arr = [1, 2, 3, 4]

print("Recursive Reverse:")
print_reverse_recursive(arr)   # Output: 4 3 2 1
print("\nIterative Reverse:")
print_reverse_iterative(arr)   # Output: 4 3 2 1