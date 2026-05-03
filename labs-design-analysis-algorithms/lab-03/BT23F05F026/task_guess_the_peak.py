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
def peak_value(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m
    return arr[l]

print(peak_value([1, 3, 7, 12, 9, 5, 2]))  # 12
print(peak_value([0, 2, 4, 6, 3, 1]))      # 6
