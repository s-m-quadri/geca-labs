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
def find_peak_in_mountain_array(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1  # Peak is to the right
        else:
            high = mid  # Peak is at mid or to the left

    return arr[low]


# Test cases
print(find_peak_in_mountain_array([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak_in_mountain_array([0, 2, 4, 6, 3, 1]))      # Output: 6
