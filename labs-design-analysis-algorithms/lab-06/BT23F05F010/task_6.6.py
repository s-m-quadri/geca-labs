def kruskal_mst_adjlist(edges, V):
    parent = [i for i in range(V)]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if xroot != yroot:
            parent[yroot] = xroot

    mst_edges = []
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))

    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return mst_edges, adj_list

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, adj_list = kruskal_mst_adjlist(edges, 4)
print(mst_edges)
for k in adj_list:
    print(f"{k}: {adj_list[k]}")
