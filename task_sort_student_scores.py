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

def merge(students, left, mid, right):
    i, j = left, mid + 1
    temp = []

    while i <= mid and j <= right:
        
        if (students[i][1] > students[j][1]) or \
           (students[i][1] == students[j][1] and students[i][0] < students[j][0]):
            temp.append(students[i])
            i += 1
        else:
            temp.append(students[j])
            j += 1

    while i <= mid:
        temp.append(students[i])
        i += 1
    while j <= right:
        temp.append(students[j])
        j += 1

    # Copy back into original list
    for k in range(len(temp)):
        students[left + k] = temp[k]


def merge_sort(students, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(students, left, mid)
        merge_sort(students, mid + 1, right)
        merge(students, left, mid, right)


def sort_students(students):
    merge_sort(students, 0, len(students) - 1)
    return students


students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
result = sort_students(students)
print(result)

