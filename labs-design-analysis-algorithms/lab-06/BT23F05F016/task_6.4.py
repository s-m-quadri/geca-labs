# Task 6.4: Find and Union Functions
# -----------------------------------

def initialize_parent(V):
    """Initialize parent array for Union-Find"""
    return [i for i in range(V)]

def find(parent, x):
    """
    Recursively find the root parent of x.
    
    Parameters:
        parent : list
            Parent array of Union-Find.
        x : int
            Vertex to find root of.
    
    Returns:
        int : Root parent of x
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])  # recursion to find root

def union(parent, x, y):
    """
    Merge sets containing x and y.
    
    Parameters:
        parent : list
            Parent array of Union-Find.
        x, y : int
            Vertices to union
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # attach root_y to root_x


# Example Test
V = 4
parent = initialize_parent(V)
print("Initial parent:", parent)

union(parent, 0, 1)
print("After union(0,1):", parent)
print("find(1):", find(parent, 1))

union(parent, 1, 2)
print("After union(1,2):", parent)
print("find(2):", find(parent, 2))
