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
# Step 1: Union-Find with path compression
def initialize_parent(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) 
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False


def kruskal_mst(num_vertices, edges):
    parent = initialize_parent(num_vertices)
    mst = []
    sorted_edges = sorted(edges, key=lambda x: x[2])

    for u, v, w in sorted_edges:
        if union(parent, u, v):
            mst.append((u, v, w))
            if len(mst) == num_vertices - 1:
                break
    return mst

def build_adjacency_list(mst_edges):
    adj = {}
    for u, v, _ in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

def visualize_mst(mst_edges):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
    plt.show()


edges = [(0, 1, 10), (0, 3, 5), (1, 3, 15), (2, 3, 4), (1, 2, 20)]
num_vertices = 4

mst = kruskal_mst(num_vertices, edges)
print("MST edges:", mst)

adj_list = build_adjacency_list(mst)
print("\nAdjacency list of MST:")
for node in sorted(adj_list):
    print(f"{node}: {adj_list[node]}")


