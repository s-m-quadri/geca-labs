# binary_search.py
# Basic binary search implementations using recursion
# Follow along to see the classic binary search in action!

def binary_search_recursive(arr, low, high, x):
    """
    Recursive binary search implementation.
    
    Args:
        arr: A sorted array to search in
        low: Starting index of current search range
        high: Ending index of current search range
        x: Target value to find
    
    Returns:
        Index of x if found, -1 otherwise
    """
    # Base case: if search range is invalid
    if low > high:
        return -1
        
    # Find middle point
    mid = (low + high) // 2
    
    # If element is present at the middle
    if arr[mid] == x:
        return mid
        
    # If element is smaller than mid, search in left half
    elif arr[mid] > x:
        return binary_search_recursive(arr, low, mid - 1, x)
        
    # Else search in right half
    else:
        return binary_search_recursive(arr, mid + 1, high, x)

# Test cases
if __name__ == "__main__":
    print("Testing binary search implementation...")
    
    # Test case 1: Basic search
    arr1 = [1, 3, 5, 7, 9, 11]
    x1 = 7
    result1 = binary_search_recursive(arr1, 0, len(arr1)-1, x1)
    print(f"\nTest 1: Searching for {x1} in {arr1}")
    print(f"Result: {result1}")
    print(f"Verification: {'Success' if result1 == 3 else 'Failed'}")
    
    # Test case 2: Element at start
    arr2 = [1, 3, 5, 7, 9]
    x2 = 1
    result2 = binary_search_recursive(arr2, 0, len(arr2)-1, x2)
    print(f"\nTest 2: Searching for {x2} in {arr2}")
    print(f"Result: {result2}")
    print(f"Verification: {'Success' if result2 == 0 else 'Failed'}")
    
    # Test case 3: Element at end
    x3 = 9
    result3 = binary_search_recursive(arr2, 0, len(arr2)-1, x3)
    print(f"\nTest 3: Searching for {x3} in {arr2}")
    print(f"Result: {result3}")
    print(f"Verification: {'Success' if result3 == 4 else 'Failed'}")
    
    # Test case 4: Element not present
    x4 = 6
    result4 = binary_search_recursive(arr2, 0, len(arr2)-1, x4)
    print(f"\nTest 4: Searching for {x4} in {arr2}")
    print(f"Result: {result4}")
    print(f"Verification: {'Success' if result4 == -1 else 'Failed'}")
    
    # Test case 5: Empty array
    arr5 = []
    x5 = 1
    result5 = binary_search_recursive(arr5, 0, len(arr5)-1, x5)
    print(f"\nTest 5: Searching for {x5} in {arr5}")
    print(f"Result: {result5}")
    print(f"Verification: {'Success' if result5 == -1 else 'Failed'}")
