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
def visualize_mst(edges, V):
    mst, total_weight = kruskal_mst(edges, V)
    adj = {i: [] for i in range(V)}
    for u, v, w in mst:
        adj[u].append(v)
        adj[v].append(u)
    for k in adj:
        print(f"{k}: {adj[k]}")
    return mst, total_weight, adj
