# -------------------------------------------
# TASK: Print Elements of Array in Reverse
# -------------------------------------------

#solution
def print_reverse_recursive(arr):
    """Prints array elements in reverse order using recursion."""
    def helper(idx):
        if idx < 0:
            return
        print(arr[idx], end=' ')
        helper(idx - 1)
    helper(len(arr) - 1)
    print()


def print_reverse_iterative(arr):
    """Prints array elements in reverse order using a loop."""
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=' ')
    print()


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Recursive:")
    print_reverse_recursive(arr)
    print("Iterative:")
    print_reverse_iterative(arr)