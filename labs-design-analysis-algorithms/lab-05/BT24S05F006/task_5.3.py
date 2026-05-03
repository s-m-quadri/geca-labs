def updateKeys(graph, u, key, parent, mstSet):
    n = len(graph)
    for v in range(n):
        if graph[u][v] != 0 and mstSet[v] == False and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


# Test case
graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]
u = 0
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

updateKeys(graph, u, key, parent, mstSet)

print("key:", key)      
print("parent:", parent) 
