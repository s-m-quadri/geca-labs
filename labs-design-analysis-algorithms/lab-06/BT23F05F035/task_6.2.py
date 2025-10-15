# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.


def sort_edges_by_weight(edge_list):

    sorted_edges = sorted(edge_list, key=lambda x: x[2])
    return sorted_edges

# Example
input_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 5), (1, 3, 2)]
sorted_edges = sort_edges_by_weight(input_edges)

print("Original Edges:", input_edges)
print("Sorted Edges by Weight:", sorted_edges)

