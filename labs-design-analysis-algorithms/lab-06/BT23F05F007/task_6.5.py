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
# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------

# --- Step 1: Find function ---
def find(parent, x):
    """
    Finds the root parent of x recursively.
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])


# --- Step 2: Union function ---
def union(parent, x, y):
    """
    Merges sets containing x and y.
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # connect one root to another


# --- Step 3: Kruskal’s algorithm ---
def kruskal(n, edges):
    """
    Builds the Minimum Spanning Tree (MST) using Kruskal’s Algorithm.
