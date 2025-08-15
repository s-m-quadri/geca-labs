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
    """
    Recursively prints elements of arr from last to first.
    """
    if index is None:
        index = len(arr) - 1  # Start at the last index

    if index < 0:
        return  # Base case: no more elements

    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)
