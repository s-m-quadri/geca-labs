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

# Task 6.1: Representing Graph Edges
# ----------------------------------

def store_edges(edge_list):
    """
    edge_list: list of tuples (u, v, w)
    u, v -> vertices
    w -> weight of edge
    Returns: list of edges
    """
    edges = []
    for edge in edge_list:
        edges.append(edge)
    return edges


# Example usage
edges_input = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
edges = store_edges(edges_input)

print("Stored Edges:", edges)
