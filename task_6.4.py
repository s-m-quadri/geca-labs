# Task 6.4: Find and Union Functions
# -----------------------------------
# Extend union-find with:
# 1. find(x) -> returns root parent of x.
# 2. union(x, y) -> merges sets containing x and y.

# Example:
# parent = [0,1,2,3]
# union(0,1) → parent updated
# find(1) → should return 0 after union

# Hint: Use recursion for find().
# Tip: Try multiple unions, like (0,1), (1,2).

def find(parent, x):
    """Find root parent of x using recursion."""
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    """Union two sets containing x and y."""
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x

# Test the functions
if __name__ == "__main__":
    # Initialize parent array
    parent = [0, 1, 2, 3]
    print("Initial parent:", parent)
    
    # Test union operations
    print("\nPerforming union(0, 1):")
    union(parent, 0, 1)
    print("Parent after union(0,1):", parent)
    print("find(1):", find(parent, 1))
    
    print("\nPerforming union(1, 2):")
    union(parent, 1, 2)
    print("Parent after union(1,2):", parent)
    print("find(2):", find(parent, 2))
    
    # Test multiple finds
    print("\nFinding roots:")
    for i in range(len(parent)):
        print(f"find({i}) = {find(parent, i)}")
