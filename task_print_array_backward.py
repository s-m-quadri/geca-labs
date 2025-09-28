def print_reverse_recursive(arr, index=None):
    if index is None:
        index = len(arr) - 1
    if index < 0:
        return
    print(arr[index], end=" ")
    print_reverse_recursive(arr, index - 1)

def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")

arr = [1, 2, 3, 4]
print("Recursive reverse:")
print_reverse_recursive(arr)

print("\nIterative reverse:")
print_reverse_iterative(arr)
