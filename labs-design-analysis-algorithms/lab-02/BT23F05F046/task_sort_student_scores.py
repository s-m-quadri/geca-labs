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

def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left_half = merge_sort(students[:mid])
    right_half = merge_sort(students[mid:])

    return merge(left_half, right_half)     

def merge(left, right):     

    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i][1] > right[j][1]) or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list      


students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort(students)
print(sorted_students)  # Output: [('Bob', 92), ('David', 92), ('Alice', 85), ('Charlie', 78)]