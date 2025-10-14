
def store_edges(edge_list):
	"""
	Accepts a list of edges as tuples (u, v, w) and returns the list.
	"""
	return edge_list

if __name__ == "__main__":
	edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
	stored = store_edges(edges)
	print("Stored edges:", stored)
