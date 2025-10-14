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


# ---------- Helper Functions (Union-Find) ----------
def create_parent_array(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    # Path compression for efficiency
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x


# ---------- Kruskal’s Algorithm ----------
def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])
    parent = create_parent_array(n)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    print("✅ MST Edges:", mst_edges)
    print("✅ Total MST Weight:", total_weight)

    return mst_edges, total_weight


# ---------- Build Adjacency List ----------
def build_adjacency_list(mst_edges):
    adj = {}
    for u, v, _ in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj


# ---------- Main Execution ----------
edges_input = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst_edges, _ = kruskal(4, edges_input)

# Build adjacency list
adj_list = build_adjacency_list(mst_edges)

print("\n✅ MST Adjacency List:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")


# ---------- (Optional) Visualization ----------
try:
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (Kruskal’s Algorithm)")
    plt.show()

except ImportError:
    print("\n⚠️ NetworkX or Matplotlib not installed. Skipping visualization.")
