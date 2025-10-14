# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the "gap" without checking every element.
# - Challenge: handle edge cases at the start and end of the array.

def find_smallest_missing_positive(arr):
    """
    Find the smallest missing positive integer in a sorted array.
    
    Args:
        arr: A sorted array of positive integers
        
    Returns:
        The smallest positive integer that is missing from arr
    """
    # If array is empty or first element > 1, return 1
    if not arr or arr[0] > 1:
        return 1
        
    # Binary search to find missing number
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If value at mid is equal to position + 1
        # then smallest missing must be in right half
        if arr[mid] == mid + 1:
            left = mid + 1
        # If value at mid is greater than position + 1
        # then smallest missing must be in left half
        else:
            right = mid - 1
            
    # First position where value != position + 1 
    return left + 1

# Test cases
if __name__ == "__main__":
    print("Testing find smallest missing positive implementation...")
    
    # Test case 1: Missing number in middle
    arr1 = [1, 2, 3, 5, 6]
    result1 = find_smallest_missing_positive(arr1)
    print(f"\nTest 1: Finding missing number in {arr1}")
    print(f"Result: {result1}")
    print(f"Verification: {'Success' if result1 == 4 else 'Failed'}")
    
    # Test case 2: Missing first number
    arr2 = [2, 3, 4, 5]
    result2 = find_smallest_missing_positive(arr2)
    print(f"\nTest 2: Finding missing number in {arr2}")
    print(f"Result: {result2}")
    print(f"Verification: {'Success' if result2 == 1 else 'Failed'}")
    
    # Test case 3: Empty array
    arr3 = []
    result3 = find_smallest_missing_positive(arr3)
    print(f"\nTest 3: Finding missing number in {arr3}")
    print(f"Result: {result3}")
    print(f"Verification: {'Success' if result3 == 1 else 'Failed'}")
    
    # Test case 4: No missing numbers until end
    arr4 = [1, 2, 3, 4]
    result4 = find_smallest_missing_positive(arr4)
    print(f"\nTest 4: Finding missing number in {arr4}")
    print(f"Result: {result4}")
    print(f"Verification: {'Success' if result4 == 5 else 'Failed'}")
    
    # Test case 5: Single element
    arr5 = [2]
    result5 = find_smallest_missing_positive(arr5)
    print(f"\nTest 5: Finding missing number in {arr5}")
    print(f"Result: {result5}")
    print(f"Verification: {'Success' if result5 == 1 else 'Failed'}")
    
    print("\nBonus: Let's understand how binary search helps:")
    arr = [1, 2, 3, 5, 6]
    print(f"For array {arr}:")
    print("Binary search compares index+1 with value")
    for i, num in enumerate(arr):
        print(f"At index {i}: Expected={i+1}, Actual={num}")
    print("First mismatch indicates missing number!")
