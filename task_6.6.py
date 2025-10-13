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
import networkx as nx
import matplotlib.pyplot as plt

def initialize_union_find(n):
    return [i for i in range(n)]

def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal(n, edges):
    parent = initialize_union_find(n)
    edges.sort(key=lambda x: x[2])
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if union(u, v, parent):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

def build_adjacency_list(mst):
    adj = {}
    for u, v, _ in mst:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    return adj

def print_adjacency_list(adj):
    for node in sorted(adj):
        print(f"{node}: {adj[node]}")

def visualize_mst(mst):
    G = nx.Graph()
    for u, v, w in mst:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()

# Example usage
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
n = 4
mst, weight = kruskal(n, edges)
adj = build_adjacency_list(mst)
print("MST edges:", mst)
print("Total weight:", weight)
print("Adjacency List:")
print_adjacency_list(adj)
visualize_mst(mst)
