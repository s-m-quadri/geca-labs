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
    Stores graph edges represented as (u, v, w) in a list.

    Parameters:
    edge_list (list of tuples): Each tuple is (u, v, w), representing an edge from u to v with weight w.

    Returns:
    list: A list containing all the edge tuples.
    """
    edges = edge_list  # Store the input list directly
    print("Stored Edges:", edges)  # Optional: for verification
    return edges

# Example usage:
edges = store_edges([(0, 1, 4), (0, 2, 3), (1, 2, 1)])

