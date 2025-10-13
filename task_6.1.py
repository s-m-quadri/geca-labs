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
# graph_edges.py
# Task 6.1: Representing Graph Edges

def store_edges(edges):
    """
    Store graph edges in a list of tuples.
    
    Parameters:
    - edges: list of tuples (u, v, w)
    
    Returns:
    - List of edges
    """
    # Simply return the edges as a list
    return edges


# Example usage
edges_input = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
edges_list = store_edges(edges_input)
print("Edges of the graph:")
for u, v, w in edges_list:
    print(f"Edge from {u} to {v} with weight {w}")

