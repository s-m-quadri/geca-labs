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

# Recursive version
def print_reverse_recursive(arr, index=None):
    if index is None:
        index = len(arr) - 1
    
    if index < 0:
        return
    
    print(arr[index])
    print_reverse_recursive(arr, index - 1)

# Iterative version
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

# Test both functions
test_array = [1, 2, 3, 4, 5]
print("Original array:", test_array)

print("\nRecursive reverse:")
print_reverse_recursive(test_array)

print("\nIterative reverse:")
print_reverse_iterative(test_array)
