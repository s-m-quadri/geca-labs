# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5

def count_occurrences(arr, target):
    """
    Count occurrences of target in sorted array arr using binary search to find first and last index.
    Returns 0 if not found.
    """
    def lower_bound(a, x):
        low, high = 0, len(a)
        while low < high:
            mid = (low + high) // 2
            if a[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low

    def upper_bound(a, x):
        low, high = 0, len(a)
        while low < high:
            mid = (low + high) // 2
            if a[mid] <= x:
                low = mid + 1
            else:
                high = mid
        return low

    lb = lower_bound(arr, target)
    ub = upper_bound(arr, target)
    return max(0, ub - lb)


if __name__ == "__main__":
    examples = [
        ([1, 2, 2, 2, 3, 4], 2),
        ([5, 5, 5, 5, 5], 5),
        ([1, 2, 3], 4),
    ]
    for arr, tgt in examples:
        print(arr, "target=", tgt, "count=", count_occurrences(arr, tgt))
