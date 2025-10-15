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

def kruskal(n, edges):
    parent = [i for i in range(n)]
    mst = []
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
    return mst

def mst_to_adjacency_list(mst_edges, n):
    adj = {i: [] for i in range(n)}
    for u, v, _ in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    n = 4
    mst = kruskal(n, edges)
    print("MST edges:", mst)
    adj = mst_to_adjacency_list(mst, n)
    print("Adjacency list:")
    for node in adj:
        print(f"{node}: {adj[node]}")
