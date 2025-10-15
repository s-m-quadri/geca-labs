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
    Given a mountain array (strictly increasing then strictly decreasing),
    return the peak element's value.
    """
    if not arr:
        raise ValueError("Array must be non-empty")
    if len(arr) == 1:
        return arr[0]

    low, high = 0, len(arr) - 1
    # Invariant: peak is somewhere in [low, high]
    while low < high:
        mid = (low + high) // 2
        # If mid is on the increasing slope, peak is to the right
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            # arr[mid] >= arr[mid+1] -> peak is at mid or to the left
            high = mid
    # low == high -> index of peak
    return arr[low]


# Example usage / tests
print(find_peak_in_mountain([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak_in_mountain([0, 2, 4, 6, 3, 1]))      # Output: 6
print(find_peak_in_mountain([1]))                     # Output: 1
