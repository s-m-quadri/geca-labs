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
    """Print elements of arr in reverse order using recursion."""
    if index is None:
        index = len(arr) - 1  # Start from the last index
    if index < 0:
        return  # Base case: if index is negative, stop recursion
    print(arr[index], end=' ')  # Print current element
    print_reverse_recursive(arr, index - 1)  # Recursive call with decremented index
def print_reverse_iterative(arr):
    """Print elements of arr in reverse order using iteration."""
    for i in range(len(arr) - 1, -1, -1):  # Loop from last index to first
        print(arr[i], end=' ')  # Print current element
# Example usage
if __name__ == "__main__":
    example_array = [1, 2, 3, 4]
    print("Recursive reverse:")
    print_reverse_recursive(example_array)
    print("\nIterative reverse:")
    print_reverse_iterative(example_array)
    print()  