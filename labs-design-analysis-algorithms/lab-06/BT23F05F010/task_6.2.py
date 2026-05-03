def sort_edges_by_weight(edges):
    return sorted(edges, key=lambda x: x[2])

edges = [(0,1,4), (0,2,3), (1,2,1)]
sorted_edges = sort_edges_by_weight(edges)
print(sorted_edges)
