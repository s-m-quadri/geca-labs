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
def first(arr, target):
    l, r, ans = 0, len(arr) - 1, -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            ans = m
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans

def last(arr, target):
    l, r, ans = 0, len(arr) - 1, -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            ans = m
            l = m + 1
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return ans

def count(arr, target):
    f = first(arr, target)
    if f == -1:
        return 0
    l = last(arr, target)
    return l - f + 1

arr1 = [1, 2, 2, 2, 3, 4]
arr2 = [5, 5, 5, 5, 5]

print(count(arr1, 2))
print(count(arr2, 5))
