

def initialize_prim_arrays(V):
	"""
	Initializes key, parent, and mstSet arrays for Prim's algorithm.
	Args:
		V (int): Number of vertices
	Returns:
		tuple: (key, parent, mstSet)
	"""
	key = [float('inf')] * V
	parent = [-1] * V
	mstSet = [False] * V
	return key, parent, mstSet

# Example usage and test case
if __name__ == "__main__":
	V = 4
	key, parent, mstSet = initialize_prim_arrays(V)
	print("key =", key)
	print("parent =", parent)
	print("mstSet =", mstSet)

