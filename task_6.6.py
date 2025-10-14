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

# Step 1: Union-Find setup
def create_parent(V):
    return [i for i in range(V)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x


# Step 2: Kruskal’s Algorithm
def kruskal(V, edges):
    edges = sorted(edges, key=lambda x: x[2])
    parent = create_parent(V)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight


# Step 3: Convert MST edges → Adjacency List
def mst_to_adj_list(mst_edges):
    adj = {}
    for u, v, w in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj


# Step 4: (Optional) Visualize MST using networkx
def visualize_mst(mst_edges):
    try:
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()
        for u, v, w in mst_edges:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
        plt.show()
    except ImportError:
        print("⚠️ Install networkx and matplotlib to visualize (pip install networkx matplotlib)")


# Step 5: Example test
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

V = 4
mst_edges, total_weight = kruskal(V, edges)

print("MST Edges:", mst_edges)
print("Total MST Weight:", total_weight)

adj_list = mst_to_adj_list(mst_edges)
print("\nAdjacency List of MST:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

# Uncomment to visualize MST (optional)
# visualize_mst(mst_edges)
