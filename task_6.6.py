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

def initialize_union_find(n):
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
        return True
    return False

def kruskal_mst(edges, num_vertices):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    parent = initialize_union_find(num_vertices)
    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if union(parent, u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

def build_adjacency_list(mst_edges):
    adj = {}

    for u, v, _ in mst_edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    
    return adj

def print_adjacency_list(adj):
    for node in sorted(adj.keys()):
        print(f"{node}: {sorted(adj[node])}")
