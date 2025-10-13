


def find_mountain_peak(arr):
   
    if not arr:
        raise ValueError("Array is empty.")
    n = len(arr)
    if n == 1:
        return arr[0]

    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            # rising slope: peak to the right
            left = mid + 1
        else:
            
            right = mid
    # left == right is the peak index
    return arr[left]


# Example usage / test cases
print(find_mountain_peak([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_mountain_peak([0, 2, 4, 6, 3, 1]))      # Output: 6

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

