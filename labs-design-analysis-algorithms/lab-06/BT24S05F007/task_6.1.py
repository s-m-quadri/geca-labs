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

def create_edge_list(edges):
    """
    Accepts an iterable of edge tuples (u, v, w) and returns a list of edges.
    """
    return list(edges)

if __name__ == "__main__":
    example = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
    edges = create_edge_list(example)
    print("Edges:", edges)
