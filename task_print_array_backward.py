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

# ---------------- Reverse Array Printing ----------------

# Recursive function to print array in reverse
def print_reverse_recursive(arr, index=None):
    if index is None:
        index = len(arr) - 1  # Start from last index
    if index < 0:
        return
    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)

# Iterative function to print array in reverse
def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")
    print()  # For newline


# -------------------- Main Program --------------------
if __name__ == "__main__":
    arr_input = input("Enter array elements separated by space: ")
    arr = list(map(int, arr_input.split()))

    print("\nReverse (recursive):")
    print_reverse_recursive(arr)
    print("\nReverse (iterative):")
    print_reverse_iterative(arr)
