# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5

def find_first_occurrence(arr, target):
    """Find the first occurrence of target using binary search"""
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid  # Found target, but keep looking for first occurrence
            high = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

def find_last_occurrence(arr, target):
    """Find the last occurrence of target using binary search"""
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid  # Found target, but keep looking for last occurrence
            low = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

def count_occurrences(arr, target):
    """Count occurrences of target in sorted array using binary search"""
    first = find_first_occurrence(arr, target)
    
    if first == -1:
        return 0  # Target not found
    
    last = find_last_occurrence(arr, target)
    return last - first + 1

# Test the function
if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 2, 2, 2, 3, 4]
    target1 = 2
    result1 = count_occurrences(arr1, target1)
    print(f"Array: {arr1}")
    print(f"Target: {target1}")
    print(f"Count: {result1}")
    print(f"Expected: 3")
    print()
    
    # Test case 2
    arr2 = [5, 5, 5, 5, 5]
    target2 = 5
    result2 = count_occurrences(arr2, target2)
    print(f"Array: {arr2}")
    print(f"Target: {target2}")
    print(f"Count: {result2}")
    print(f"Expected: 5")
    print()
    
    # Test case 3: Target not in array
    arr3 = [1, 2, 3, 4, 5]
    target3 = 6
    result3 = count_occurrences(arr3, target3)
    print(f"Array: {arr3}")
    print(f"Target: {target3}")
    print(f"Count: {result3}")
    print(f"Expected: 0")
    print()
    
    # Test case 4: Single occurrence
    arr4 = [1, 2, 3, 4, 5]
    target4 = 3
    result4 = count_occurrences(arr4, target4)
    print(f"Array: {arr4}")
    print(f"Target: {target4}")
    print(f"Count: {result4}")
    print(f"Expected: 1")
    print()
    
    # Test case 5: All elements are the same
    arr5 = [7, 7, 7, 7]
    target5 = 7
    result5 = count_occurrences(arr5, target5)
    print(f"Array: {arr5}")
    print(f"Target: {target5}")
    print(f"Count: {result5}")
    print(f"Expected: 4")
