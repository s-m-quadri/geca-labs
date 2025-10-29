# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1

def smallest_missing_positive(sorted_pos):
    """
    Given a sorted list of positive integers (ascending), return the smallest missing positive integer.
    Uses binary search to find the first index where arr[i] != i+1.
    Example:
      [1,2,3,5,6] -> 4
      [2,3,4]     -> 1
    """
    n = len(sorted_pos)
    if n == 0:
        return 1
    # if first element > 1 -> 1 is missing
    if sorted_pos[0] > 1:
        return 1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        expected = mid + 1
        if sorted_pos[mid] == expected:
            low = mid + 1
        else:
            # arr[mid] > expected (since positive sorted) -> gap is at or before mid
            high = mid - 1
    # low is the count of consecutive 1..k present, so missing is low+1
    return low + 1


if __name__ == "__main__":
    tests = [
        [1, 2, 3, 5, 6],
        [2, 3, 4, 5],
        [],
        [1, 2, 3, 4],
        [1, 1, 2, 3],  # duplicates handled — still finds first missing
    ]
    for t in tests:
        print(t, "->", smallest_missing_positive(t))
