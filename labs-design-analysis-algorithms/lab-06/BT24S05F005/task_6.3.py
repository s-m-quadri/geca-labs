# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.
def initialize_parent(n):
    """
    Initializes the parent array for Union-Find.
    Each element is its own parent initially.

    Parameters:
    n (int): Number of vertices.

    Returns:
    list: Parent array where parent[i] = i
    """
    parent = [i for i in range(n)]
    return parent

# Example usage:
num_vertices = 5
parent = initialize_parent(num_vertices)
print("Initialized parent array:", parent)
