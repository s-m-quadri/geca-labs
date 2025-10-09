# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------

def initialize_parent(V):
    """
    Function to initialize the parent array for Union-Find.
    Initially, each vertex is its own parent.
    
    Parameters:
        V : int
            Number of vertices in the graph.
    
    Returns:
        parent : list
            List where parent[i] = i
    """
    parent = [i for i in range(V)]
    return parent


# Example Test
V = 5
parent = initialize_parent(V)
print("Initial parent array:", parent)
