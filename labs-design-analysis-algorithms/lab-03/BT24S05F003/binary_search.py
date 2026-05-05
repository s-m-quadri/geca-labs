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
# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

def binary_search_recursive(arr, low, high, x):
    """Recursive binary search"""
    if high >= low:
        mid = (low + high) // 2  # Find the middle index

        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, it can only be in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)

        # Else, element can only be in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        # Element is not present in array
        return -1


# Try it out
arr = [1, 3, 5, 7, 9, 11]
x = 7
print("Recursive:", binary_search_recursive(arr, 0, len(arr) - 1, x))
