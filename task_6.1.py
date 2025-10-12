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
#to do later
# Task 6.1: Representing Graph Edges
# -----------------------------------

def store_edges(edges):
    """
    Accepts a list of edges as tuples (u, v, w)
    where:
        u = starting vertex
        v = ending vertex
        w = weight of the edge
    Returns the list of edges.
    """
    # Simply store and return the list
    edge_list = edges
    return edge_list


# Example usage
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
result = store_edges(edges)
print("Stored Edges:", result)
