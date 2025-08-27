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

def print_reverse_recursive(arr, index=None):
<<<<<<< HEAD:task_print_array_backward.py
    if index is None:
        index = len(arr) - 1 
    if index < 0:
        return
    print(arr[index], end=' ')
    print_reverse_recursive(arr, index - 1)

def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=' ')


arr = [1, 2, 3, 4]
print("Recursive Output:")
print_reverse_recursive(arr)
print("\nIterative Output:")
print_reverse_iterative(arr)
=======
    """
    Recursively prints elements of arr from last to first.
    """
    if index is None:
        index = len(arr) - 1  # Start at the last index

    if index < 0:
        return  # Base case: no more elements

    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)
>>>>>>> upstream/stable:labs-design-analysis-algorithms/lab-01/BT24F05F001/task_print_array_backward.py
