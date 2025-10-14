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

def merge(left, right):
    """Merge two sorted lists of student tuples."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Compare scores first (descending)
        if left[i][1] > right[j][1]:
            result.append(left[i])
            i += 1
        elif left[i][1] < right[j][1]:
            result.append(right[j])
            j += 1
        else:
            # If scores are equal, compare names (ascending)
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_students(students):
    """Sort students by scores (descending) and names (ascending if scores equal)."""
    if len(students) <= 1:
        return students
    
    # Divide the array into two halves
    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    
    # Merge the sorted halves
    return merge(left, right)
