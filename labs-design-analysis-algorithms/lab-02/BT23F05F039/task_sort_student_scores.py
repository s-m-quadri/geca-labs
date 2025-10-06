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

def compare(student1, student2):
    if student1[1] > student2[1]:
        return True
    elif student1[1] < student2[1]:
        return False
    else:
        return student1[0] < student2[0]


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(students):
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])
    return merge(left, right)

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
sorted_students = merge_sort(students)
print("Sorted Students:", sorted_students)