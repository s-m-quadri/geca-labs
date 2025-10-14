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
# -----------------------------------

def create_edge_list(edges):
    """
    Accepts edges as tuples (u, v, w)
    and stores them in a list of tuples.
    
    Parameters:
        edges (list of tuples): Each tuple represents (u, v, weight)
    
    Returns:
        list: The same list of edges
    """
    edge_list = []
    
    # Store all edges in the list
    for edge in edges:
        edge_list.append(edge)
    
    return edge_list


# Example test
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
result = create_edge_list(edges)
print("Stored Edges:", result)
