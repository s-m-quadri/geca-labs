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
def peak_in_mountain(arr):
    n = len(arr)
    if n == 0:
        return None
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return arr[low]

tests = [
    [1, 3, 7, 12, 9, 5, 2],
    [0, 2, 4, 6, 3, 1],
    [1],
    [1, 2],
    [2, 1]
]

for t in tests:
    print("Input:", t, "-> Peak:", peak_in_mountain(t))
