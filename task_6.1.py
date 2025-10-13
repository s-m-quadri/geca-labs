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
    Accepts a list of edges as (u, v, w) tuples and returns the list.
    """
    return edge_list

if __name__ == "__main__":
    # Example usage
    edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
    stored = store_edges(edges)
    print("Edges:", stored)
