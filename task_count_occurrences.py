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


def first_occurrence(arr, target):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            ans = m
            r = m - 1  # keep searching left
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans


def last_occurrence(arr, target):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            ans = m
            l = m + 1  # keep searching right
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1


def main():
    tests = [
        ([1, 2, 2, 2, 3, 4], 2),
        ([5, 5, 5, 5, 5], 5),
        ([1, 1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 6),
    ]
    for arr, target in tests:
        print(f"Input: {arr}, target={target} -> Count: {count_occurrences(arr, target)}")


if __name__ == "__main__":
    main()
