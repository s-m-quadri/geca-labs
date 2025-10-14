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

def kruskal_mst(num_vertices, edges):
	"""
	Returns MST edges and total weight using Kruskal's algorithm.
	"""
	# Sort edges by weight
	sorted_edges = sorted(edges, key=lambda x: x[2])
	parent = [i for i in range(num_vertices)]
	def find(x):
		if parent[x] != x:
			return find(parent[x])
		return x
	def union(x, y):
		root_x = find(x)
		root_y = find(y)
		if root_x != root_y:
			parent[root_y] = root_x
			return True
		return False
	mst_edges = []
	total_weight = 0
	for u, v, w in sorted_edges:
		if union(u, v):
			mst_edges.append((u, v, w))
			total_weight += w
		if len(mst_edges) == num_vertices - 1:
			break
	return mst_edges, total_weight

# Example usage
if __name__ == "__main__":
	edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
	mst, weight = kruskal_mst(4, edges)
	print("MST edges:", mst)
	print("MST total weight:", weight)
