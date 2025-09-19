
def min_key_vertex(key, mstSet):
	min_val = float('inf')
	min_index = -1
	for i in range(len(key)):
		if not mstSet[i] and key[i] < min_val:
			min_val = key[i]
			min_index = i
	return min_index

def update_keys_and_parents(graph, u, key, parent, mstSet):
	V = len(graph)
	for v in range(V):
		if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
			key[v] = graph[u][v]
			parent[v] = u

def prim_one_iteration(graph, key, parent, mstSet):
	# Select the min-key vertex not yet in MST
	u = min_key_vertex(key, mstSet)
	mstSet[u] = True
	update_keys_and_parents(graph, u, key, parent, mstSet)

# Example usage and test case
if __name__ == "__main__":
	graph = [
		[0, 1, 4],
		[1, 0, 2],
		[4, 2, 0]
	]
	key = [0, float('inf'), float('inf')]
	mstSet = [True, False, False]
	parent = [-1, -1, -1]
	prim_one_iteration(graph, key, parent, mstSet)
	print("key =", key)      # Expected: [0, 1, 2]
	print("parent =", parent)  # Expected: [-1, 0, 1]
