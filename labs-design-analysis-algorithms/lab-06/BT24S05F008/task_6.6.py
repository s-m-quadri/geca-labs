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


def kruskal_mst_adjlist(edges, V):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]
    
    def find(parent, x):
        if parent[x] != x:
            return find(parent, parent[x])
        return x
    
    def union(parent, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        if xroot != yroot:
            parent[yroot] = xroot
    
    mst_edges = []
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return mst_edges, adj_list

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, adj_list = kruskal_mst_adjlist(edges, V)
print("MST edges:", mst_edges)
print("Adjacency list:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Optional visualization
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):w for u,v,w in mst_edges})
    plt.show()
except ImportError:
    print("Install networkx and matplotlib to see the MST graph visualization.")
