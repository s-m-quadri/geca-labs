# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.

def initialize_union_find(vertices):
    parent = [i for i in range(vertices)]
    return parent

vertices = 5
parent = initialize_union_find(vertices)
print("Parent array:", parent)
