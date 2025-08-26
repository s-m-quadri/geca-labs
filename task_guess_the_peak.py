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
    if not arr:
        raise ValueError("Array must be non-empty")
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid
   
    return arr[l]  


if __name__ == "__main__":
    print(peak_in_mountain([1, 3, 7, 12, 9, 5, 2]))  
    print(peak_in_mountain([0, 2, 4, 6, 3, 1]))     