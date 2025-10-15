def kruskal_mst(edges, V):
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

    mst = []
    total_weight = 0
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal_mst(edges, 4)
print(mst_edges)
print(mst_weight)
