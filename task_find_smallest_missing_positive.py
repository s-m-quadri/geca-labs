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



def smallest_missing_positive(arr):
    n = len(arr)

    # Case 1: if the first number is > 1 → smallest missing is 1
    if arr[0] > 1:
        return 1

    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        expected = mid + 1  # what should be at index mid if no numbers missing

        if arr[mid] == expected:
            low = mid + 1   # gap must be to the right
        else:
            high = mid - 1  # gap is to the left

    # After loop, 'low' points to first missing position
    return low + 1


def main():
    tests = [
        [1, 2, 3, 5, 6],
        [2, 3, 4, 5],
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [1],
    ]
    for arr in tests:
        print(f"Input: {arr} -> Smallest missing: {smallest_missing_positive(arr)}")


if __name__ == "__main__":
    main()
