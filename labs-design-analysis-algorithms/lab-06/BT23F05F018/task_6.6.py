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

def create_parent_array(n):
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


# Step 2: Kruskal’s Algorithm
def kruskal(edges, num_vertices):
    edges = sorted(edges, key=lambda x: x[2])  # sort by weight
    parent = create_parent_array(num_vertices)
    mst = []

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
    
    return mst


# Step 3: Convert MST edges → Adjacency List
def build_adjacency_list(mst):
    adj = {}
    for u, v, w in mst:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    return adj



edges_input = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4

mst_edges = kruskal(edges_input, num_vertices)
adj_list = build_adjacency_list(mst_edges)

print("MST Edges:", mst_edges)
print("\nAdjacency List:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")



try:
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
    plt.show()

except ImportError:
    print("\nVisualization skipped (install networkx & matplotlib to see MST graph).")

