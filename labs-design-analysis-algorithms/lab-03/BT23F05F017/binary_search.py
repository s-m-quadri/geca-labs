# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

def binary_search_recursive(arr, low, high, x):
    """Recursive binary search"""
    # TODO

# Try it out
arr = [1, 3, 5, 7, 9, 11]
x = 7
print("Recursive:", binary_search_recursive(arr, 0, len(arr)-1, x))

def binary_search_recursive(arr, low, high, x):
    """Recursive binary search"""
    # Base case: element not found
    if low > high:
        return -1

    # Calculate middle index
    mid = (low + high) // 2

    # Found the element
    if arr[mid] == x:
        return mid

    # Element is in the left half
    elif x < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, x)

    # Element is in the right half
    else:
        return binary_search_recursive(arr, mid + 1, high, x)

# Try it out
arr = [1, 3, 5, 7, 9, 11]