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
# union_find.py
# Task 6.4: Union-Find with find() and union()

def find(parent, x):
    """
    Find the root parent of x using recursion.
    
    Parameters:
    - parent: list of parent pointers
    - x: element to find
    
    Returns:
    - Root parent of x
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])  # Recursive call


def union(parent, x, y):
    """
    Merge sets containing x and y.
    
    Parameters:
    - parent: list of parent pointers
    - x, y: elements to union
    
    Returns:
    - None (parent array is updated in-place)
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x  # Merge y's set into x's set


# Example usage
n = 4
parent = [i for i in range(n)]
print("Initial parent array:", parent)

union(parent, 0, 1)
print("After union(0,1):", parent)

union(parent, 1, 2)
print("After union(1,2):", parent)

print("find(2) →", find(parent, 2))  # Should return 0
print("find(3) →", find(parent, 3))  # Should return 3
