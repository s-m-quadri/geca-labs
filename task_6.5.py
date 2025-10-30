# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.

def kruskal(edges):
    """
    Build MST using Kruskal's algorithm.
    edges: iterable of (u, v, w)
    Returns (mst_edges_list, total_weight)
    """
    edges = list(edges)
    if not edges:
        return [], 0

    # determine number of vertices (assumes vertices are integer labels)
    max_vertex = max(max(u, v) for u, v, _ in edges)
    parent = [i for i in range(max_vertex + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst = []
    total_weight = 0

    for u, v, w in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

if __name__ == "__main__":
    graph = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    mst_edges, weight = kruskal(graph)
    print("MST edges:", mst_edges)
    print("MST weight =", weight)
