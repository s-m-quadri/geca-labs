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
    Finds the peak index and peak value in a mountain array (strictly increases then strictly decreases).
    Returns a tuple (peak_index, peak_value). If array empty, returns (None, None).
    """
    if not arr:
        return None, None
    n = len(arr)
    # If array length is 1, it's the peak
    if n == 1:
        return 0, arr[0]

    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        # Compare with right neighbor to decide slope direction
        if arr[mid] < arr[mid + 1]:
            # ascending slope -> peak is to the right
            low = mid + 1
        else:
            # descending slope (or mid is peak) -> peak is at mid or to the left
            high = mid

    # low == high is the peak index
    return low, arr[low]


# Example test cases
print(find_peak_in_mountain([1, 3, 7, 12, 9, 5, 2]))  # -> (3, 12)
print(find_peak_in_mountain([0, 2, 4, 6, 3, 1]))      # -> (3, 6)
print(find_peak_in_mountain([1]))                     # -> (0, 1)


