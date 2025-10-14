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


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

def kruskal_mst(edges, n):
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(n)]
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

def build_adjacency_list(mst, n):
    adj = {i: [] for i in range(n)}
    for u, v, _ in mst:
        adj[u].append(v)
        adj[v].append(u)
    return adj

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
n = 4
mst, total_weight = kruskal_mst(edges, n)
print("MST edges:", mst)
print("Total weight:", total_weight)

adj_list = build_adjacency_list(mst, n)
print("Adjacency list of MST:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

# Optional visualization
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    for u, v, w in mst:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
except ImportError:
    print("NetworkX or matplotlib not installed, skipping visualization.")
