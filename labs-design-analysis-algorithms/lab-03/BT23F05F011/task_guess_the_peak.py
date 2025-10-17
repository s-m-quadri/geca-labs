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
def find_peak(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        # If mid is less than mid+1, peak is to the right
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            # If mid is greater than mid+1, peak is at mid or to the left
            right = mid

    # When left == right, we found the peak
    return arr[left]

# Test cases
print(find_peak([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak([0, 2, 4, 6, 3, 1]))      # Output: 6

