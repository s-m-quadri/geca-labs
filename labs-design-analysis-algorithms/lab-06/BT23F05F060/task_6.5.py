
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
#
def find(x, parent):
	if parent[x] != x:
		return find(parent[x], parent)
	return x

def union(x, y, parent):
	x_root = find(x, parent)
	y_root = find(y, parent)
	if x_root != y_root:
		parent[y_root] = x_root

def kruskal_mst(num_vertices, edges):
	parent = [i for i in range(num_vertices)]
	mst_edges = []
	total_weight = 0
	sorted_edges = sorted(edges, key=lambda x: x[2])
	for u, v, w in sorted_edges:
		if find(u, parent) != find(v, parent):
			union(u, v, parent)
			mst_edges.append((u, v, w))
			total_weight += w
	print("MST edges:", mst_edges)
	print("MST total weight:", total_weight)
	return mst_edges, total_weight

# Example usage
if __name__ == "__main__":
	edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
	num_vertices = 4
	kruskal_mst(num_vertices, edges)
