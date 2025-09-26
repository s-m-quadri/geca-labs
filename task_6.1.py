# Task 6.1: Representing Graph Edges
# -----------------------------------
# Write a function that accepts edges as tuples (u, v, w).
# u, v are vertices, w is the weight.
# Store all edges in a list of tuples.

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected storage: Same list, but sorted is NOT required here.

# Hint: Just create and return the list.
# Tip: Print the list to verify edges.
def represent_edges(edges):
    """
    Accepts edges as tuples (u, v, w) and stores them in a list.
    
    Args:
        edges: List of tuples (u, v, w) where u, v are vertices and w is weight
    
    Returns:
        List of edge tuples
    """
    return edges

# Test the function
if __name__ == "__main__":
    edges = [(0,1,4), (0,2,3), (1,2,1)]
    result = represent_edges(edges)
    print("Original edges:", result)