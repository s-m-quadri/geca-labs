# Puzzle / Learning focus:
# - You are given a “mountain array” (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.
#
# Example test cases:
# Input: [1, 3, 7, 12, 9, 5, 2]
# Output: 12
#
# Input: [0, 2, 4, 6, 3, 1]
# Output: 6

def find_peak_in_mountain(arr):
    """
    Returns the peak value in a mountain array (strictly increases then strictly decreases).
    """
    if not arr:
        raise ValueError("Array must be non-empty")
    n = len(arr)
    if n == 1:
        return arr[0]

    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            
            high = mid
    
    return arr[low]


# Example 
print(find_peak_in_mountain([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak_in_mountain([0, 2, 4, 6, 3, 1]))      # Output: 6
