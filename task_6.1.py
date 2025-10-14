def store_edges(edge_list):
    """
    Accepts edges as tuples (u, v, w) and stores them in a list.

    edge_list: list of tuples (u, v, w)
    Returns: list of edges
    """
    # Simply return a copy to avoid modifying the original list
    return list(edge_list)

# Example usage
input_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
edges = store_edges(input_edges)

print("Edges stored:", edges)
