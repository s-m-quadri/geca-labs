# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the "gap" without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1

def find_smallest_missing_positive(arr):
    """
    Find the smallest missing positive integer in a sorted array.
    Uses binary search logic to efficiently locate the gap.
    """
    # Edge case: empty array
    if not arr:
        return 1
    
    # Edge case: first element is not 1
    if arr[0] != 1:
        return 1
    
    # Edge case: array is consecutive starting from 1
    if arr == list(range(1, len(arr) + 1)):
        return len(arr) + 1
    
    # Binary search for the first gap
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # If arr[mid] == mid + 1, then all elements from 0 to mid are consecutive
        # The gap must be in the right half
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            # There's a gap before mid, search in left half
            high = mid - 1
    
    # The missing number is at position 'low' (0-indexed), so the number is low + 1
    return low + 1

def find_smallest_missing_positive_linear(arr):
    """
    Linear approach for comparison/verification.
    This is O(n) but less efficient than binary search O(log n).
    """
    expected = 1
    for num in arr:
        if num == expected:
            expected += 1
        elif num > expected:
            break
    return expected

# Test the function
if __name__ == "__main__":
    # Test case 1
    arr1 = [1, 2, 3, 5, 6]
    result1 = find_smallest_missing_positive(arr1)
    linear1 = find_smallest_missing_positive_linear(arr1)
    print(f"Array: {arr1}")
    print(f"Binary search result: {result1}")
    print(f"Linear result: {linear1}")
    print(f"Expected: 4")
    print()
    
    # Test case 2
    arr2 = [2, 3, 4, 5]
    result2 = find_smallest_missing_positive(arr2)
    linear2 = find_smallest_missing_positive_linear(arr2)
    print(f"Array: {arr2}")
    print(f"Binary search result: {result2}")
    print(f"Linear result: {linear2}")
    print(f"Expected: 1")
    print()
    
    # Test case 3: Consecutive array
    arr3 = [1, 2, 3, 4, 5]
    result3 = find_smallest_missing_positive(arr3)
    linear3 = find_smallest_missing_positive_linear(arr3)
    print(f"Array: {arr3}")
    print(f"Binary search result: {result3}")
    print(f"Linear result: {linear3}")
    print(f"Expected: 6")
    print()
    
    # Test case 4: Gap at the beginning
    arr4 = [3, 4, 5, 6]
    result4 = find_smallest_missing_positive(arr4)
    linear4 = find_smallest_missing_positive_linear(arr4)
    print(f"Array: {arr4}")
    print(f"Binary search result: {result4}")
    print(f"Linear result: {linear4}")
    print(f"Expected: 1")
    print()
    
    # Test case 5: Single element
    arr5 = [2]
    result5 = find_smallest_missing_positive(arr5)
    linear5 = find_smallest_missing_positive_linear(arr5)
    print(f"Array: {arr5}")
    print(f"Binary search result: {result5}")
    print(f"Linear result: {linear5}")
    print(f"Expected: 1")
    print()
    
    # Test case 6: Empty array
    arr6 = []
    result6 = find_smallest_missing_positive(arr6)
    linear6 = find_smallest_missing_positive_linear(arr6)
    print(f"Array: {arr6}")
    print(f"Binary search result: {result6}")
    print(f"Linear result: {linear6}")
    print(f"Expected: 1")