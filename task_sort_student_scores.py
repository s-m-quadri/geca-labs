
def compare(a, b):
    """Return True if tuple `a` should come before tuple `b`."""
    # Primary: higher score first
    # Secondary: alphabetical order if scores are equal
    return (a[1] > b[1]) or (a[1] == b[1] and a[0] < b[0])


def merge_sort_students(students):
    """Perform merge sort on list of student (name, score) tuples."""
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_students(students[:mid])
    right = merge_sort_students(students[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two sorted halves based on the comparison logic."""
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


# Example test cases
if __name__ == "__main__":
    # Test 1: Basic example
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
    print(merge_sort_students(students))

    # Test 2: All same scores (should sort alphabetically)
    students = [("Zoe", 90), ("Anna", 90), ("Mike", 90)]
    print(merge_sort_students(students))


    # Test 3: All different scores (just descending by score)
    students = [("A", 10), ("B", 30), ("C", 20)]
    print(merge_sort_students(students))

