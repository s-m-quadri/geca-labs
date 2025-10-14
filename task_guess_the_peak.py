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
    """
    Returns the peak value and its index in a mountain array.
    Assumes arr has length >= 1 and contains a single peak (strictly increasing then strictly decreasing).
    """
    n = len(arr)
    if n == 1:
        return arr[0], 0
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        # compare with right neighbour (safe because mid < high when low < high)
        if arr[mid] < arr[mid + 1]:
            # rising slope -> peak to the right
            low = mid + 1
        else:
            # descending slope (or peak at mid) -> peak at or to the left
            high = mid
    # low == high is the peak index
    return arr[low], low

# Example tests:
print(find_peak([1, 3, 7, 12, 9, 5, 2]))  # -> (12, 3)
print(find_peak([0, 2, 4, 6, 3, 1]))      # -> (6, 3)
print(find_peak([1]))                     # -> (1, 0)
