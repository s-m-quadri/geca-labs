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

def merge_and_count(arr, left, mid, right):
    
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i = 0  
    j = 0 
    k = left  
    inv_count = 0

    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            
            inv_count += (len(left_part) - i)
        k += 1

    
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inv_count


def merge_sort_and_count(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

       
        inv_count += merge_sort_and_count(arr, left, mid)
       
        inv_count += merge_sort_and_count(arr, mid+1, right)
        
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count


def count_inversions(arr):
    
    arr_copy = arr[:]
    return merge_sort_and_count(arr_copy, 0, len(arr_copy)-1)



if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    print("Array:", arr)
    result = count_inversions(arr)
    print("Number of inversions:", result)