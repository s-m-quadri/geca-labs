# Task 6.6: Challenge - Visualize MST
# -------------------------------------
# Extend Kruskal’s algorithm:
# 1. Input edges and build MST.
# 2. Print MST edges in adjacency list format.
# 3. (Optional for extra) Use networkx + matplotlib to plot MST.

# Example:
# MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# Expected adjacency list:
# 0: [1, 3]
# 1: [0]
# 2: [3]
# 3: [0, 2]

# Hint: Use dictionary for adjacency list.
# Tip: Visualization part is optional, but fun for testing.

def kruskal_mst(num_vertices, edges):
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
	for u, v, w in sorted_edges:
		if union(u, v):
			mst_edges.append((u, v, w))
		if len(mst_edges) == num_vertices - 1:
			break
	return mst_edges

def print_adjacency_list(num_vertices, mst_edges):
	adj = {i: [] for i in range(num_vertices)}
	for u, v, _ in mst_edges:
		adj[u].append(v)
		adj[v].append(u)
	for node in adj:
		print(f"{node}: {adj[node]}")

# Optional: Visualization
def visualize_mst(mst_edges):
	try:
		import networkx as nx
		import matplotlib.pyplot as plt
	except ImportError:
		print("networkx or matplotlib not installed. Skipping visualization.")
		return
	G = nx.Graph()
	for u, v, w in mst_edges:
		G.add_edge(u, v, weight=w)
	pos = nx.spring_layout(G)
	edge_labels = {(u, v): w for u, v, w in mst_edges}
	nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
	plt.title("MST Visualization")
	plt.show()

# Example usage
if __name__ == "__main__":
	edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
	num_vertices = 4
	mst_edges = kruskal_mst(num_vertices, edges)
	print("MST edges:", mst_edges)
	print("Adjacency list:")
	print_adjacency_list(num_vertices, mst_edges)
	# Uncomment below to visualize (requires networkx and matplotlib)
	# visualize_mst(mst_edges)
