
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
#
def store_edges(edges):
	"""
	Accepts a list of edge tuples (u, v, w) and prints them.
	Returns the list of edges.
	"""
	print("Edges:", edges)
	return edges


if __name__ == "__main__":
	edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
	store_edges(edges)
