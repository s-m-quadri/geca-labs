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
def find_peak_index(arr):
    """
    Return the index of the peak in a mountain array.
    Assumes arr is a mountain array (strictly increases then strictly decreases).
    """
    if not arr:
        return None
    low, high = 0, len(arr) - 1
    # Invariant: peak index is in [low, high]
    while low < high:
        mid = (low + high) // 2
        # If mid is before the peak, arr[mid] < arr[mid+1], move right
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            # arr[mid] >= arr[mid+1], peak is at mid or to the left
            high = mid
    # low == high == peak index
    return low

def find_peak_value(arr):
    idx = find_peak_index(arr)
    return None if idx is None else arr[idx]

# Example usage
a1 = [1, 3, 7, 12, 9, 5, 2]
a2 = [0, 2, 4, 6, 3, 1]

print(find_peak_value(a1))  # 12
print(find_peak_value(a2))  # 6
