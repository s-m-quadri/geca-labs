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

def print_reverse_recursive(arr, idx=None):
    if idx is None:
        idx = len(arr) - 1
    if idx < 0:
        return
    print(arr[idx], end=' ')
    print_reverse_recursive(arr, idx - 1)

def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=' ')

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Recursive:")
    print_reverse_recursive(arr)
    print("\nIterative:")
    print_reverse_iterative(arr)
    print()
