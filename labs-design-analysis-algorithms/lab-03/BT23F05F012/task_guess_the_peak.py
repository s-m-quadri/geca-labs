# Puzzle / Learning focus:#
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
def find_peak_index(arr):
    """
    Return index of the peak element in a mountain array.
    If arr is empty return -1. For arrays of length 1 return 0.
    Assumes a mountain: strictly increasing then strictly decreasing.
    """
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        return 0

    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        # Compare with right neighbor to decide slope direction
        if arr[mid] < arr[mid + 1]:
            # We're on the increasing slope → peak is to the right
            low = mid + 1
        else:
            # We're on the decreasing slope → peak is at mid or to the left
            high = mid
    # low == high is the peak index
    return low

def find_peak_value(arr):
    idx = find_peak_index(arr)
    return None if idx == -1 else arr[idx]


# Example tests
a1 = [1, 3, 7, 12, 9, 5, 2]
a2 = [0, 2, 4, 6, 3, 1]

print(find_peak_index(a1), find_peak_value(a1))  # -> 3 12
print(find_peak_index(a2), find_peak_value(a2))  # -> 3 6

