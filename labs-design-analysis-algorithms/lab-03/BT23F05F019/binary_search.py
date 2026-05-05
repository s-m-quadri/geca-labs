# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

def binary_search_recursive(arr, low, high, x):
    """Recursive binary search"""
    # Base case: element not found
    if low > high:
        return -1
    
    # Calculate mid point
    mid = (low + high) // 2
    
    # Element found at mid
    if arr[mid] == x:
        return mid
    
    # Element is smaller than mid, search left half
    elif x < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, x)
    
    # Element is larger than mid, search right half
    else:
        return binary_search_recursive(arr, mid + 1, high, x)

def binary_search_iterative(arr, x):
    """Iterative binary search for comparison"""
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

# Try it out
arr = [1, 3, 5, 7, 9, 11]
x = 7
print("Array:", arr)
print("Searching for:", x)
print("Recursive result:", binary_search_recursive(arr, 0, len(arr)-1, x))
print("Iterative result:", binary_search_iterative(arr, x))

print("\nTesting with different values:")
for target in [1, 5, 11, 4, 12]:
    recursive_result = binary_search_recursive(arr, 0, len(arr)-1, target)
    iterative_result = binary_search_iterative(arr, target)
    print(f"Target {target}: Recursive={recursive_result}, Iterative={iterative_result}")
