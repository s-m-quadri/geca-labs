#def initialize_parent(n):
    return [i for i in range(n)]

def find(parent, x):
    """
    Finds the root parent of x using recursion.
    
    Parameters:
    parent (list): The parent array.
    x (int): The element to find the root of.
    
    Returns:
    int: Root parent of x.
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """
    Merges the sets that contain x and y.

    Parameters:
    parent (list): The parent array.
    x (int), y (int): Elements to union.
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # Attach y's root to x's root
