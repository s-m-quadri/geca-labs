# Given a list of tuples containing student names and scores:
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
# Sort them in:
#     - Descending order of scores
#     - If scores are equal, ascending alphabetical order by name

# Expected Output:
# [("Bob", 92), ("David", 92), ("Alice", 85), ("Charlie", 78)]

# INSTRUCTIONS:
# - Implement merge sort to achieve the required sorting order.
# - Modify the comparison logic inside merge function accordingly.
# - Do not use Python's built-in sort().

# Write your solution here
def merge_and_sort(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        # Compare: first by score descending, then by name ascending
        if arr[i][1] > arr[j][1] or (arr[i][1] == arr[j][1] and arr[i][0] < arr[j][0]):
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
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

    for x in range(left, right + 1):
        arr[x] = temp[x]

def merge_sort_students(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_students(arr, temp, left, mid)
        merge_sort_students(arr, temp, mid + 1, right)
        merge_and_sort(arr, temp, left, mid, right)

def sort_students(students):
    temp = [0] * len(students)
    merge_sort_students(students, temp, 0, len(students) - 1)
    return students

# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = sort_students(students)
print(sorted_students)
