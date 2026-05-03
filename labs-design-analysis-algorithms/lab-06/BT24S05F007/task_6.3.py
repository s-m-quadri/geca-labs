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
    Create and return a parent list for union-find with n vertices.
    parent[i] = i
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return [i for i in range(n)]

if __name__ == "__main__":
    print("Parent for 5 vertices:", make_parent(5))
