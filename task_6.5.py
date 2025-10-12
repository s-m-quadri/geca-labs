# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.

# Solution:

def find(parent, x):
	if parent[x] != x:
		return find(parent, parent[x])
	return x

def union(parent, x, y):
	root_x = find(parent, x)
	root_y = find(parent, y)
	if root_x != root_y:
		parent[root_y] = root_x

def kruskal_mst(num_vertices, edges):
	"""
	Builds MST using Kruskal's algorithm.
	Returns MST edges and total weight.
	"""
	parent = [i for i in range(num_vertices)]
	sorted_edges = sorted(edges, key=lambda x: x[2])
	mst_edges = []
	total_weight = 0
	for u, v, w in sorted_edges:
		if find(parent, u) != find(parent, v):
			union(parent, u, v)
			mst_edges.append((u, v, w))
			total_weight += w
	print("MST edges:", mst_edges)
	print("MST total weight:", total_weight)
	return mst_edges, total_weight

if __name__ == "__main__":
	edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
	kruskal_mst(4, edges)