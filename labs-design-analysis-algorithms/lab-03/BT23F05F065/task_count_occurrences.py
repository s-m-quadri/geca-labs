# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.

def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of target in sorted array.
    
    Args:
        arr: A sorted array
        target: Value to find
        
    Returns:
        Index of first occurrence of target, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            first_occurrence = mid
            # Continue searching in left half
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return first_occurrence

def find_last_occurrence(arr, target):
    """
    Find the index of the last occurrence of target in sorted array.
    
    Args:
        arr: A sorted array
        target: Value to find
        
    Returns:
        Index of last occurrence of target, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    last_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            last_occurrence = mid
            # Continue searching in right half
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last_occurrence

def count_occurrences(arr, target):
    """
    Count occurrences of target in sorted array using binary search.
    
    Args:
        arr: A sorted array
        target: Value to count
        
    Returns:
        Number of occurrences of target in arr
    """
    # Find first and last occurrences
    first = find_first_occurrence(arr, target)
    
    # If element is not present
    if first == -1:
        return 0
        
    last = find_last_occurrence(arr, target)
    
    # Return count = last - first + 1
    return last - first + 1

# Test cases
if __name__ == "__main__":
    print("Testing count occurrences implementation...")
    
    # Test case 1: Multiple occurrences in middle
    arr1 = [1, 2, 2, 2, 3, 4]
    target1 = 2
    result1 = count_occurrences(arr1, target1)
    print(f"\nTest 1: Counting {target1} in {arr1}")
    print(f"Result: {result1}")
    print(f"Verification: {'Success' if result1 == 3 else 'Failed'}")
    
    # Test case 2: All same elements
    arr2 = [5, 5, 5, 5, 5]
    target2 = 5
    result2 = count_occurrences(arr2, target2)
    print(f"\nTest 2: Counting {target2} in {arr2}")
    print(f"Result: {result2}")
    print(f"Verification: {'Success' if result2 == 5 else 'Failed'}")
    
    # Test case 3: Element not present
    arr3 = [1, 2, 3, 4, 5]
    target3 = 6
    result3 = count_occurrences(arr3, target3)
    print(f"\nTest 3: Counting {target3} in {arr3}")
    print(f"Result: {result3}")
    print(f"Verification: {'Success' if result3 == 0 else 'Failed'}")
    
    # Test case 4: Single occurrence
    arr4 = [1, 2, 3, 4, 5]
    target4 = 3
    result4 = count_occurrences(arr4, target4)
    print(f"\nTest 4: Counting {target4} in {arr4}")
    print(f"Result: {result4}")
    print(f"Verification: {'Success' if result4 == 1 else 'Failed'}")
    
    # Test case 5: Empty array
    arr5 = []
    target5 = 1
    result5 = count_occurrences(arr5, target5)
    print(f"\nTest 5: Counting {target5} in {arr5}")
    print(f"Result: {result5}")
    print(f"Verification: {'Success' if result5 == 0 else 'Failed'}")
    
    print("\nBonus: Let's see how first/last occurrence works:")
    arr = [1, 2, 2, 2, 3, 4]
    target = 2
    first = find_first_occurrence(arr, target)
    last = find_last_occurrence(arr, target)
    print(f"For array {arr} and target {target}:")
    print(f"First occurrence at index: {first}")
    print(f"Last occurrence at index: {last}")
    print(f"Therefore count = {last - first + 1}")
