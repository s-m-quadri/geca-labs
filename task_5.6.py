
import heapq

def prim_mst_heap(graph, start=0):
	V = len(graph)
	key = [float('inf')] * V
	parent = [-1] * V
	in_mst = [False] * V
	key[start] = 0
	min_heap = [(0, start)]  # (key, vertex)

	while min_heap:
		k, u = heapq.heappop(min_heap)
		if in_mst[u]:
			continue
		in_mst[u] = True
		for v in range(V):
			weight = graph[u][v]
			if weight and not in_mst[v] and weight < key[v]:
				key[v] = weight
				parent[v] = u
				heapq.heappush(min_heap, (key[v], v))

	mst_edges = []
	for v in range(V):
		if parent[v] != -1:
			mst_edges.append((parent[v], v, graph[parent[v]][v]))
	return mst_edges

# Example usage and test case
if __name__ == "__main__":
	graph = [
		[0, 2, 0, 6, 0],
		[2, 0, 3, 8, 5],
		[0, 3, 0, 0, 7],
		[6, 8, 0, 0, 9],
		[0, 5, 7, 9, 0]
	]
	start = 0
	result = prim_mst_heap(graph, start)
	print(result)  # Expected: [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
