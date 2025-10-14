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
    Finds the peak element in a mountain (bitonic) array.
    Returns the peak value.
    """
    if not arr:
        raise ValueError("Array must be non-empty")

    low, high = 0, len(arr) - 1

    while low < high:  # loop ends when low == high
        mid = (low + high) // 2
        # compare mid with its right neighbor
        if arr[mid] < arr[mid + 1]:
            # ascending slope -> peak is to the right
            low = mid + 1
        else:
            # descending slope -> peak is at mid or to the left
            high = mid

    # low == high is the peak index
    return arr[low]


# --------------------------
# Example Test Cases
# --------------------------
print(find_peak_in_mountain([1, 3, 7, 12, 9, 5, 2]))  # Output: 12
print(find_peak_in_mountain([0, 2, 4, 6, 3, 1]))      # Output: 6
print(find_peak_in_mountain([1, 2, 3, 4, 3, 2, 1]))   # Output: 4
print(find_peak_in_mountain([0, 1, 0]))               # Output: 1

