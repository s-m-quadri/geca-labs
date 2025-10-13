"""
Background:
Repeating iterations completes the MST construction.

Task:
Implement full Prim's algorithm for a given adjacency matrix.

Instruction:

Tip:
Use previous helper functions: min-key selection, key updates.

Test case:
graph = [
 [0, 2, 0, 6],
 [2, 0, 3, 8],
 [0, 3, 0, 0],
 [6, 8, 0, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(0,3,6)]
"""

def prim_mst(graph, start):
	V = len(graph)
	key = [float('inf')] * V
	parent = [-1] * V
	mstSet = [False] * V
	key[start] = 0
	for _ in range(V):
		# Find min-key vertex not in MST
		min_val = float('inf')
		u = -1
		for i in range(V):
			if not mstSet[i] and key[i] < min_val:
				min_val = key[i]
				u = i
		if u == -1:
			break
		mstSet[u] = True
		# Update keys and parents for neighbors
		for v in range(V):
			if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
				key[v] = graph[u][v]
				parent[v] = u
	# Collect MST edges
	mst_edges = []
	for v in range(V):
		if parent[v] != -1:
			mst_edges.append((parent[v], v, graph[v][parent[v]]))
	return mst_edges

# Test case
if __name__ == "__main__":
	graph = [
		[0, 2, 0, 6],
		[2, 0, 3, 8],
		[0, 3, 0, 0],
		[6, 8, 0, 0]
	]
	start = 0
	print(prim_mst(graph, start))  # Expected: [(0,1,2),(1,2,3),(0,3,6)]
