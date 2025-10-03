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

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return False
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return True

def kruskal_mst(edges, num_nodes):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(num_nodes)]
    rank = [0] * num_nodes
    mst_edges = []
    mst_weight = 0
    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst_edges.append((u, v, weight))
            mst_weight += weight
    return mst_edges, mst_weight

graph_edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_nodes = 4
mst, total_weight = kruskal_mst(graph_edges, num_nodes)
print("MST edges:", mst)
print("MST total weight:", total_weight)

