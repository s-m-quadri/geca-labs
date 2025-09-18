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

def merge(left, right):
    """Merge two sorted lists with custom comparison logic."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_name, left_score = left[i]
        right_name, right_score = right[j]
        
        # Compare by score (descending), then by name (ascending)
        if left_score > right_score:
            # Left has higher score, so it comes first
            result.append(left[i])
            i += 1
        elif left_score < right_score:
            # Right has higher score, so it comes first
            result.append(right[j])
            j += 1
        else:
            # Scores are equal, compare by name (ascending)
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
    """Sort students using merge sort with custom comparison."""
    if len(students) <= 1:
        return students
    
    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)

# Test the function
if __name__ == "__main__":
    # Test case 1
    students1 = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
    result1 = merge_sort_students(students1)
    print("Original students:")
    for student in students1:
        print(f"  {student}")
    print("\nSorted students (score desc, name asc):")
    for student in result1:
        print(f"  {student}")
    print(f"Expected: [('Bob', 92), ('David', 92), ('Alice', 85), ('Charlie', 78)]")
    print()
    
    # Test case 2: More complex example
    students2 = [
        ("Emma", 88), ("John", 95), ("Sarah", 88), 
        ("Mike", 95), ("Lisa", 82), ("Tom", 88)
    ]
    result2 = merge_sort_students(students2)
    print("Original students:")
    for student in students2:
        print(f"  {student}")
    print("\nSorted students (score desc, name asc):")
    for student in result2:
        print(f"  {student}")
    print()
    
    # Test case 3: Edge case with single student
    students3 = [("Single", 100)]
    result3 = merge_sort_students(students3)
    print("Single student:")
    print(f"Original: {students3}")
    print(f"Sorted: {result3}")
