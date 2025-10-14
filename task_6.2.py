def sort_edges_by_weight(edges):
    """
    Sorts a list of edges (u, v, w) by their weight w.
    """
    return sorted(edges, key=lambda x: x[2])

