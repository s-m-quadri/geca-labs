# Task 6.2: Sorting Edges
# ------------------------

def sort_edges_by_weight(edge_list):
    """
    Function to sort edges by their weight.
    Each edge is a tuple (u, v, w)
    where w is the weight.
    """
    # Sort using the 3rd element of each tuple (weight)
    sorted_edges = sorted(edge_list, key=lambda x: x[2])
    return sorted_edges


# Example Test
input_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (1, 3, 2)]
sorted_edges = sort_edges_by_weight(input_edges)
print("Sorted edges by weight:", sorted_edges)
