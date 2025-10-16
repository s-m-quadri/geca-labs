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
def store_edges(edge_list):
    """
    Accepts edges as tuples (u, v, w) and stores them in a list.

    edge_list: list of tuples (u, v, w)
    Returns: list of edges
    """
    edges = []
    for edge in edge_list:
        edges.append(edge)
    return edges

# Example usage
input_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
edges = store_edges(input_edges)

print("Edges stored:", edges)
