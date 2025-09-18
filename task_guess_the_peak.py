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

def find_peak(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return arr[left]

# Example test cases:

print(find_peak([1, 3, 7, 12, 9, 5, 2])) 
print(find_peak([0, 2, 4, 6, 3, 1]))      
print(find_peak([1, 2, 3, 4, 3, 2, 1]))   
print(find_peak([0, 5, 10, 5, 0]))        
