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


from typing import List, Optional

def find_peak_index(arr: List[int]) -> Optional[int]:
    n = len(arr)
    if n == 0:
        return None
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low

def find_peak_value(arr: List[int]) -> Optional[int]:
    idx = find_peak_index(arr)
    return None if idx is None else arr[idx]

print(find_peak_value([1, 3, 7, 12, 9, 5, 2]))
print(find_peak_value([0, 2, 4, 6, 3, 1]))