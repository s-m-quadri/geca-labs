#i dont have any idea about how to work around the networkx and matplotlib libraries so i will not be able to do the extras 

#solution
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(edges, V):
    edges.sort(key=lambda x: x[2]) 
    parent = [i for i in range(V)]
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

def build_adjacency_list(mst_edges, V):
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

# Example (very important)
edges = [
    (0, 1, 4),
    (0, 3, 5),
    (1, 3, 6),
    (1, 2, 10),
    (2, 3, 4)
]
V = 4

mst_edges, total_weight = kruskal_mst(edges, V)
adj_list = build_adjacency_list(mst_edges, V)

print("MST Edges:", mst_edges)
print("Total Weight:", total_weight)
print("Adjacency List:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")
