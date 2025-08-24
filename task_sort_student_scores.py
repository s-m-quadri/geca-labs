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
def merge_sort_students(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_students(arr[:mid])
    right = merge_sort_students(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:
            merged.append(left[i])
            i += 1
        elif left[i][1] < right[j][1]:
            merged.append(right[j])
            j += 1
        else:  
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort_students(students)
print(sorted_students)
