# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.


def create_parent_array(num_vertices):
    
    parent = [i for i in range(num_vertices)]
    return parent

vertices = 5
parent = create_parent_array(vertices)

print("Number of vertices:", vertices)
print("Initial parent array:", parent)

