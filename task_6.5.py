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


def create_parent_array(num_vertices):
    return [i for i in range(num_vertices)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])  

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  

def kruskal_mst(edges, num_vertices):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    parent = create_parent_array(num_vertices)
    mst_edges = []
    total_weight = 0

    for u, v, w in sorted_edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        if root_u != root_v:
            union(parent, root_u, root_v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight


edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_vertices = 4

mst, weight = kruskal_mst(edges, num_vertices)

print("Edges in the MST:", mst)
print("Total weight of MST:", weight)


