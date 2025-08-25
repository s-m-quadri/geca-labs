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

count = 0

def merge_count(left, right):
    result = []
    i = j = 0
    global count
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count = count + len(left) - i
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result 

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr 
    mid = len(arr) // 2
    left = merge_sort_count(arr[:mid])
    right = merge_sort_count(arr[mid:])

    return merge_count(left,right)

if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    merge_sort_count(arr)
    print("Total inversions are",count)