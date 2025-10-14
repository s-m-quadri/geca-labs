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
# Task 6.6: Challenge - Visualize MST
# -------------------------------------

# Step 1: Kruskal's Algorithm (reuse from Task 6.5)
def create_parent(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(vertices, edges):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = create_parent(vertices)
    mst_edges = []
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    return mst_edges

# Step 2: Convert MST edges to adjacency list
def mst_to_adjacency_list(mst_edges, vertices):
    adj_list = {i: [] for i in range(vertices)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

# Step 3: Optional - visualize using networkx
def plot_mst(mst_edges):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Example usage
vertices = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst_edges = kruskal_mst(vertices, edges)
print("MST edges:", mst_edges)

adj_list = mst_to_adjacency_list(mst_edges, vertices)
print("Adjacency List of MST:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

# Optional visualization (requires networkx and matplotlib)
# plot_mst(mst_edges)
