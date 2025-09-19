
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

def prim_mst(graph, start=0):
	V = len(graph)
	key = [float('inf')] * V
	parent = [-1] * V
	mstSet = [False] * V
	key[start] = 0
	for _ in range(V):
		u = min_key_vertex(key, mstSet)
		mstSet[u] = True
		update_keys_and_parents(graph, u, key, parent, mstSet)
	mst_edges = []
	for v in range(V):
		if parent[v] != -1:
			mst_edges.append((parent[v], v, graph[parent[v]][v]))
	return mst_edges

# Example usage and test case
if __name__ == "__main__":
	graph = [
		[0, 2, 0, 6],
		[2, 0, 3, 8],
		[0, 3, 0, 0],
		[6, 8, 0, 0]
	]
	start = 0
	result = prim_mst(graph, start)
	print(result)  # Expected: [(0, 1, 2), (1, 2, 3), (0, 3, 6)]
