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
def bs_mountain_arr(arr,low,high):
    if low == high:
        return arr[low]

    mid = (low+high)//2
    if arr[mid] > arr[mid+1]:
        return bs_mountain_arr(arr,low,mid)
    else:
        return bs_mountain_arr(arr,mid+1,high)

arr = [1, 3, 7, 12, 9, 5, 2]
print("Output:",bs_mountain_arr(arr,0,len(arr)-1))