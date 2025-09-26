# -------------------------------------------
# Problem: Print array backward
# Example: [1,2,3] → 3 2 1
# -------------------------------------------

def print_array_backward_recursive(arr, i=None):
    if i is None:
        i = len(arr) - 1
    if i < 0:
        return
    print(arr[i])
    print_array_backward_recursive(arr, i - 1)

def print_array_backward_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

if __name__ == "__main__":
    arr = input("Enter array elements separated by space: ").split()
    print("Recursive:")
    print_array_backward_recursive(arr)
    print("\nIterative:")
    print_array_backward_iterative(arr)
