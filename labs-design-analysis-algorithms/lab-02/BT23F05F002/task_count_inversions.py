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

def merge_and_count(arr, temp, left, mid, right):
    inv_count = 0
    i, j, k = left, mid + 1, left
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    
    return inv_count

def count_inversions(arr):
    temp = [0] * len(arr)
    arr_copy = arr.copy()
    return merge_sort_and_count(arr_copy, temp, 0, len(arr) - 1)

test_array = [2, 4, 1, 3, 5]
result = count_inversions(test_array)
print(f"Array: {test_array}")
print(f"Number of inversions: {result}")

test_array2 = [5, 4, 3, 2, 1]
result2 = count_inversions(test_array2)
print(f"Array: {test_array2}")
print(f"Number of inversions: {result2}")

