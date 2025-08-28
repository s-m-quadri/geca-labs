# Given an array of integers, count the number of inversions in the array.
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

# Example:
# Input: [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The inversions are (2,1), (4,1), (4,3)

# INSTRUCTIONS:
# - Implement a function using Merge Sort modification to count inversions efficiently.
# - Target time complexity: O(n log n)
# - Do not use brute force O(n^2) method.

# Write your solution here
def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j] and i<j:
           result= result+1
           i+=1  
        else:
            j += 1
    
    return result

def merge_sort(arr):
    """Basic recursive merge sort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted:", sorted_arr)

