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

def binary_search_smpi(arr,low,high):
    if low>high:
        return low+1

    mid=(low+high)//2
    if arr[mid]==mid+1:
        return binary_search_smpi(arr,mid+1,high)
    else:
        return binary_search_smpi(arr,low,mid-1)

arr = [1, 2, 3, 4]
print("Output:", binary_search_smpi(arr,0,len(arr)-1))