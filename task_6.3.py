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
    Initialize parent array for union-find where parent[i] = i.
    
    Args:
        n: Number of vertices
    
    Returns:
        List where parent[i] = i for all i from 0 to n-1
    """
    return [i for i in range(n)]

# Test the function
if __name__ == "__main__":
    n = 5
    parent = initialize_parent(n)
    print(f"Parent array for {n} vertices:", parent)
