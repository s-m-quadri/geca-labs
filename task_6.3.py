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
    """Initialize union-find parent array where each element is its own parent."""
    return [i for i in range(n)]

# Alternative implementation
def make_set(n):
    """Create parent array for n vertices."""
    return list(range(n))

# Test the function
if __name__ == "__main__":
    # Test case 1
    n1 = 5
    parent1 = initialize_union_find(n1)
    print(f"Parent array for {n1} vertices:", parent1)
    
    # Test case 2
    n2 = 7
    parent2 = make_set(n2)
    print(f"Parent array for {n2} vertices:", parent2)
    
    # Verify each element is its own parent
    print("Verification: Each element is its own parent:", all(parent1[i] == i for i in range(len(parent1))))
