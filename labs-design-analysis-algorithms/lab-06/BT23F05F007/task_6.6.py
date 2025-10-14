# Task 6.6: Challenge - Visualize MST
# -------------------------------------

import networkx as nx
import matplotlib.pyplot as plt

# --- Step 1: Union-Find helper functions ---
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x


# --- Step 2: Kruskal’s MST Function ---
def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(n)]
    mst_edges = []
    mst_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            mst_weight += w

    return mst_edges, mst_weight


# --- Step 3: Build adj
