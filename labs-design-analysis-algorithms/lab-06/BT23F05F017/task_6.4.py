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
    """
    Find the root parent of x using recursion.
    
    Args:
        parent: Parent array
        x: Element to find root of
    
    Returns:
        Root parent of x
    """
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    """
    Merge sets containing x and y.
    
    Args:
        parent: Parent array
        x: First element
        y: Second element
    """
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        parent[root_x] = root_y

if __name__ == "__main__":
    parent = [0, 1, 2, 3]
    print("Initial parent:", parent)

    union(parent, 0, 1)
    print("After union(0,1):", parent)
    print("find(1):", find(parent, 1))

    union(parent, 1, 2)
    print("After union(1,2):", parent)
    print("find(2):", find(parent, 2))