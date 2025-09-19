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
    """Merge two sorted lists with custom comparison for student scores."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Compare scores first (descending), then names (ascending)
        left_name, left_score = left[i]
        right_name, right_score = right[j]
        
        if left_score > right_score:  # Higher score comes first
            result.append(left[i])
            i += 1
        elif left_score < right_score:  # Lower score comes later
            result.append(right[j])
            j += 1
        else:  # Same score, sort by name alphabetically (ascending)
            if left_name <= right_name:
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
    """Sort students by score (descending) then by name (ascending) using merge sort."""
    if len(students) <= 1:
        return students
    
    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    
    return merge(left, right)

if __name__ == "__main__":
    # Test case from the example
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
    print("Original students:", students)
    sorted_students = merge_sort_students(students)
    print("Sorted students:", sorted_students)
    print("Expected: [('Bob', 92), ('David', 92), ('Alice', 85), ('Charlie', 78)]")
    
    # Additional test cases
    print("\nAdditional test cases:")
    
    # Test with more students and same scores
    students2 = [("Eve", 90), ("Frank", 85), ("Grace", 90), ("Henry", 85), ("Ivy", 95)]
    print("Students 2:", students2)
    sorted_students2 = merge_sort_students(students2)
    print("Sorted students 2:", sorted_students2)
    
    # Test with all same scores
    students3 = [("Zoe", 80), ("Alice", 80), ("Bob", 80)]
    print("Students 3:", students3)
    sorted_students3 = merge_sort_students(students3)
    print("Sorted students 3:", sorted_students3)
