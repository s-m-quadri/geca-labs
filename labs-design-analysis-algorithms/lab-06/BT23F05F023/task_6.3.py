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
    """
    Creates and returns a parent array for union-find,
    where parent[i] = i initially.
    """
    return [i for i in range(num_vertices)]

# Example usage:
if __name__ == "__main__":
    num_vertices = 5
    parent = create_parent_array(num_vertices)
    print(parent)
