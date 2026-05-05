def print_reverse_recursive(arr, i=None):
    if i is None:
        i = len(arr) - 1
    if i < 0:
        return
    print(arr[i], end=" ")
    print_reverse_recursive(arr, i - 1)

def print_reverse_iterative(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")

arr = [1, 2, 3, 4]
print_reverse_recursive(arr)
print()
print_reverse_iterative(arr)
