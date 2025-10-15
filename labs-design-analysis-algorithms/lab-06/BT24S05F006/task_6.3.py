# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.
# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------

def create_parent(n):
    """
    n: number of vertices
    Returns: parent list where each vertex is its own parent initially
    """
    parent = [i for i in range(n)]
    return parent


# Example usage
n = int(input("Enter number of vertices: "))
parent = create_parent(n)

print("Initial parent array:", parent)
