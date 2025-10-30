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
    Find and return the peak value in a "mountain" array (strictly increases then strictly decreases).
    Uses binary search: if arr[mid] < arr[mid+1] move right, else move left.
    """
    if not arr:
        raise ValueError("array is empty")
    n = len(arr)
    if n == 1:
        return arr[0]
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        # compare to neighbor to decide slope direction
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return arr[low]


if __name__ == "__main__":
    examples = [
        [1, 3, 7, 12, 9, 5, 2],
        [0, 2, 4, 6, 3, 1],
        [1],
    ]
    for ex in examples:
        print(find_peak(ex))
