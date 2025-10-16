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
# Kruskal + adjacency list visualization
import networkx as nx
import matplotlib.pyplot as plt

def kruskal_mst_adjlist(edges, V):
    # Step 1: Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Union-Find
    parent = [i for i in range(V)]
    
    def find(x):
        if parent[x] == x:
