# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.

def initialize_parent(V):
    parent = [i for i in range(V)]
    return parent

V = 15
parent = initialize_parent(V)
print("Parent Array:", parent)