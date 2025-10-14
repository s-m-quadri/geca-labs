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
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal(n, edges):
    parent = create_parent_array(n)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst = []

    for u, v, w in sorted_edges:
        if union(parent, u, v):
            mst.append((u, v, w))

    return mst

def build_adjacency_list(mst_edges):
    adj = {}
    for u, v, _ in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj


edges_input = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4

mst_edges = kruskal(num_vertices, edges_input)
adj_list = build_adjacency_list(mst_edges)

print("MST Edges:", mst_edges)
print("\nAdjacency List:")
for node in sorted(adj_list):
    print(f"{node}: {adj_list[node]}")
