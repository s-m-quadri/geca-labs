# Puzzle / Learning focus:
# - You are given a "mountain array" (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.
#
# Example test cases:
# Input: [1, 3, 7, 12, 9, 5, 2]
# Output: 12
#
# Input: [0, 2, 4, 6, 3, 1]
# Output: 6

def find_peak(arr):
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is the peak
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        
        # If right neighbor is greater, peak is to the right
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        
        # If left neighbor is greater or equal, peak is to the left
        else:
            right = mid
    
    return arr[left]

# Test cases
arr1 = [1, 3, 7, 12, 9, 5, 2]
print(f"Input: {arr1}")
print(f"Peak element: {find_peak(arr1)}")

arr2 = [0, 2, 4, 6, 3, 1]
print(f"\nInput: {arr2}")
print(f"Peak element: {find_peak(arr2)}")
# Completed the program
