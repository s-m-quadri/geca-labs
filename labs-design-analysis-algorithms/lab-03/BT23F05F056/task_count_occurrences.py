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
def binarySearch(arr, target):
    l = 0
    h = len(arr) -1
    first = -1
    while l<= h:
        mid = (l+h)//2
        if arr[mid] == target:
            first = mid
            h = mid -1
        elif arr[mid] > target:
            h = mid -1
        else:
            l = mid+1

    if first == -1:
        return 0

    l = 0
    h = len(arr) -1
    last = - 1
    while l<= h:
        mid = (l+h)//2
        if arr[mid] == target:
            last = mid
            l = mid +1
        elif arr[mid] > target:
            h = mid -1
        else :
            l = mid+1
    
    return last - first + 1

arr = [1, 2, 2, 2, 3, 4]
target = 2
print("No. of times target appears is:", binarySearch(arr, target))