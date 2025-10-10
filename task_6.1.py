# Task 6.1: Representing Graph Edges
# -----------------------------------
# Write a functidefon that accepts edges as tuples (u, v, w).
# u, v are vertices, w is the weight.
# Store all edges in a list of tuples.

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected storage: Same list, but sorted is NOT required here.

# Hint: Just create and return the list.
# Tip: Print the list to verify edges.
 store_edges(edge_list):
    """
    Accepts a list of edges where each edge is represented as a tuple (u, v, w),
    with u and v as vertices and w as the weight of the edge.
    
    Returns the list of edges.
    """
    edges = edge_list
    return edges

# Example usage:
edges = store_edges([(0, 1, 4), (0, 2, 3), (1, 2, 1)])
print("Stored edges:", edges)
#output
Stored edges: [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
