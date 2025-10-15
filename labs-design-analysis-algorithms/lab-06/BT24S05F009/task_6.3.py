# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.

def make_parent(n):
    """
    Initializes and returns a parent array for n vertices.
    Each vertex is its own parent initially.
    """
    return [i for i in range(n)]

if __name__ == "__main__":
    n = 5
    parent = make_parent(n)
    print("Initial parent array:", parent)
