
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
	"""
	Sorts a list of edges (u, v, w) by their weight w.
	"""
	return sorted(edge_list, key=lambda x: x[2])

if __name__ == "__main__":
	edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (2, 3, 7), (1, 3, 2)]
	sorted_edges = sort_edges_by_weight(edges)
	print("Sorted edges:", sorted_edges)
