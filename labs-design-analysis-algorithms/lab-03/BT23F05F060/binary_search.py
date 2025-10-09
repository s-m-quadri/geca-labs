# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

# Recursive binary search
def binary_search_recursive(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, x)
    else:
        return binary_search_recursive(arr, mid + 1, high, x)
 
# Iterative binary search
def binary_search_iterative(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
 
# Driver
arr = [1, 3, 5, 7, 9, 11]
x = 7
print("Recursive:", binary_search_recursive(arr, 0, len(arr)-1, x))
print("Iterative:", binary_search_iterative(arr, x))
