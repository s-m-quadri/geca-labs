def store_edges(edge_list):
    edges = []
    for u, v, w in edge_list:
        edges.append((u, v, w))
    return edges

edge_list = [(0,1,4), (0,2,3), (1,2,1)]
edges = store_edges(edge_list)
print(edges)
