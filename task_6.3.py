def initialize_union_find(V):
    """
    Initialize parent array for Union-Find.

    V: number of vertices
    Returns: parent array where each vertex is its own parent initially
    """
    parent = [i for i in range(V)]  # each vertex is its own parent
    return parent

# Example usage
V = 5
parent = initialize_union_find(V)
print("Initial parent array:", parent)
