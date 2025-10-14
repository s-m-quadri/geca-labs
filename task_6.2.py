def sort_edges_by_weight(edges):
    """
    Sort edges based on their weight.

    edges: list of tuples (u, v, w)
    Returns: sorted list of edges
    """
    return sorted(edges, key=lambda x: x[2])  # sort by weight (3rd element of tuple)

# Example usage
edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 2), (3, 0, 5)]
sorted_edges = sort_edges_by_weight(edges)

print("Edges sorted by weight:", sorted_edges)
