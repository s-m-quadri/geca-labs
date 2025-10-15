# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.

def initialize_union_find(n):
    """
    Initializes the Union-Find parent array.

    Parameters:
    n (int): Number of vertices.

    Returns:
    list: A list where parent[i] = i initially.
    """
    parent = [i for i in range(n)]
    print("Initial parent array:", parent)  # Optional: for verification
    return parent

# Example usage:
parent = initialize_union_find(5)
