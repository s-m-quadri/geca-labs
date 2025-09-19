
def min_key_vertex(key, mstSet):
	"""
	Finds the index of the vertex with the minimum key value not yet included in MST.
	Args:
		key (list of float): Key values for vertices
		mstSet (list of bool): MST inclusion status for vertices
	Returns:
		int: Index of the minimum key vertex not in MST
	"""
	min_val = float('inf')
	min_index = -1
	for i in range(len(key)):
		if not mstSet[i] and key[i] < min_val:
			min_val = key[i]
			min_index = i
	return min_index

# Example usage and test case
if __name__ == "__main__":
	key = [0, 2, 3]
	mstSet = [True, False, False]
	print(min_key_vertex(key, mstSet))  # Expected output: 1
