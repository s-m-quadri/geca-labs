# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

def binary_search_recursive(arr, low, high, x):
    """Recursive binary search"""
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search_recursive(arr, low, mid - 1, x)
    else:
        return binary_search_recursive(arr, mid + 1, high, x)

# Try it out
arr = [1, 3, 5, 7, 9, 11]
x = 7
print("Recursive:", binary_search_recursive(arr, 0, len(arr)-1, x))
# Completed the program