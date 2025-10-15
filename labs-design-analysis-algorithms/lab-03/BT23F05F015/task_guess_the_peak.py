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
    Finds peak element in a mountain array (strictly increasing then strictly decreasing).
    Returns (peak_index, peak_value).
    Time complexity: O(log n), Space: O(1)
    """
    if not arr:
        return None, None

    low, high = 0, len(arr) - 1

    # Binary search variant: while low < high
    while low < high:
        mid = (low + high) // 2
        # If mid is on the rising slope, peak is to the right
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            # arr[mid] >= arr[mid+1] => peak is at mid or to the left
            high = mid

    # low == high is the peak index
    return low, arr[low]


# Example tests
a1 = [1, 3, 7, 12, 9, 5, 2]
idx1, val1 = find_peak_in_mountain(a1)
print("Peak index:", idx1, "Peak value:", val1)  # Peak value: 12

a2 = [0, 2, 4, 6, 3, 1]
idx2, val2 = find_peak_in_mountain(a2)
print("Peak index:", idx2, "Peak value:", val2)  # Peak value: 6

