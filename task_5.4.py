def prim_iteration(graph, key, parent, mstSet):
    u = min_key_vertex(key, mstSet)
    mstSet[u] = True
    update_neighbors(graph, u, key, parent, mstSet)

graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

prim_iteration(graph, key, parent, mstSet)
prim_iteration(graph, key, parent, mstSet)

print("key =", key)
print("parent =", parent)
