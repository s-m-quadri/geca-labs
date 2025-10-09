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
# ------------------------------------
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[ry] < rank[rx]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
    return True

def kruskal(n, edges):
    edges_sorted = sorted(edges, key=lambda e: (e[2], min(e[0], e[1]), max(e[0], e[1])))
    parent = [i for i in range(n)]
    rank = [0] * n
    mst = []
    total_weight = 0

    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            a, b = (u, v) if u <= v else (v, u)
            mst.append((a, b, w))
            total_weight += w

    mst.sort(key=lambda e: (e[2], e[0], e[1]))
    return mst, total_weight

def build_adjacency_list(mst, n):
    adj = {i: [] for i in range(n)}
    for u, v, w in mst:
        adj[u].append(v)
        adj[v].append(u)
    for k in adj:
        adj[k].sort()
    return adj

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4

mst, weight = kruskal(n, edges)
adj_list = build_adjacency_list(mst, n)

print("MST Edges:", mst)
print("Total MST Weight:", weight)
print("\nAdjacency List:")
for i in range(n):
    print(f"{i}: {adj_list[i]}")
