# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.
# union_find_basic.py
# Task 6.3: Union-Find Data Structure (Basics)

def initialize_union_find(n):
    """
    Initialize a parent array for union-find.
    
    Parameters:
    - n: number of vertices
    
    Returns:
    - parent array where parent[i] = i
    """
    parent = [i for i in range(n)]
    return parent


# Example usage
n = 5
parent = initialize_union_find(n)
print(f"Initial parent array for {n} vertices: {parent}")
