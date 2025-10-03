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
def compare(a, b):
    # Returns True if a should come before b
    return (a[1] > b[1]) or (a[1] == b[1] and a[0] < b[0])

def merge_sort_students(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    merged = []
    
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


# Example usage
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
print(merge_sort_students(students))
