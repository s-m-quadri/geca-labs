# Puzzle / Learning focus:
# - You are given a "mountain array" (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.

def find_peak(arr):
    """
    Find the peak element in a mountain array using binary search.
    A mountain array increases then decreases, with a single peak.
    
    Args:
        arr: A mountain array (first increases then decreases)
        
    Returns:
        The peak element in the array
    """
    # Handle edge cases
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
        
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is less than next element
        # peak must be in right half
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        # If mid element is greater than next element
        # peak must be in left half (including mid)
        else:
            right = mid
            
    # When left == right, we've found the peak
    return arr[left]

# Test cases
if __name__ == "__main__":
    print("Testing find peak implementation...")
    
    # Test case 1: Peak in middle, longer array
    arr1 = [1, 3, 7, 12, 9, 5, 2]
    result1 = find_peak(arr1)
    print(f"\nTest 1: Finding peak in {arr1}")
    print(f"Result: {result1}")
    print(f"Verification: {'Success' if result1 == 12 else 'Failed'}")
    
    # Test case 2: Peak in middle, shorter array
    arr2 = [0, 2, 4, 6, 3, 1]
    result2 = find_peak(arr2)
    print(f"\nTest 2: Finding peak in {arr2}")
    print(f"Result: {result2}")
    print(f"Verification: {'Success' if result2 == 6 else 'Failed'}")
    
    # Test case 3: Empty array
    arr3 = []
    result3 = find_peak(arr3)
    print(f"\nTest 3: Finding peak in {arr3}")
    print(f"Result: {result3}")
    print(f"Verification: {'Success' if result3 == None else 'Failed'}")
    
    # Test case 4: Single element
    arr4 = [5]
    result4 = find_peak(arr4)
    print(f"\nTest 4: Finding peak in {arr4}")
    print(f"Result: {result4}")
    print(f"Verification: {'Success' if result4 == 5 else 'Failed'}")
    
    # Test case 5: Two elements
    arr5 = [3, 1]
    result5 = find_peak(arr5)
    print(f"\nTest 5: Finding peak in {arr5}")
    print(f"Result: {result5}")
    print(f"Verification: {'Success' if result5 == 3 else 'Failed'}")
    
    print("\nBonus: Understanding the binary search approach:")
    arr = [1, 3, 7, 12, 9, 5, 2]
    print(f"For array {arr}:")
    print("Binary search compares elements with their neighbors:")
    for i in range(len(arr)-1):
        print(f"Position {i}: {arr[i]} → {arr[i+1]}: {'Increasing' if arr[i] < arr[i+1] else 'Decreasing'}")
    print("Peak is where we transition from increasing to decreasing!")
