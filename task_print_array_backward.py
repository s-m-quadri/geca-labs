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
#to do task

# Function 1: Recursive approach
def print_reverse_recursive(arr, index=None):
    if index is None:   # Start from last element
        index = len(arr) - 1
    
    if index < 0:   # Base case: stop when index goes out of bounds
        return
    
    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)  # Recursive call


# Function 2: Iterative approach
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):  # Loop from end to start
        print(arr[i], end=" ")


# -------------------------------
# Example Usage
arr = [1, 2, 3, 4]

print("Recursive Output:")
print_reverse_recursive(arr)
print("\nIterative Output:")
print_reverse_iterative(arr)

