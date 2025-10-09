"""
Background:
Prim's algorithm repeats selection and update steps to build MST.

Task:
Combine selection of min-key vertex and neighbor updates in one iteration.

Instruction:
- Implement one iteration of Prim's loop.
- Do not complete entire MST yet.

Tip:
Test on small 3-4 vertex graphs to check updates.

Test case:
graph = [
 [0, 1, 4],
 [1, 0, 2],
 [4, 2, 0]
]
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after iteration:
# key = [0, 1, 2]
# parent = [-1, 0, 1]
"""
def min_key_vertex(key, mstSet):
    min_value = float('inf')
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    return min_index


def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


def prim_one_iteration(graph, key, parent, mstSet):
  
    u = min_key_vertex(key, mstSet)
    mstSet[u] = True  
    
    
    update_keys(graph, u, key, parent, mstSet)


# Test case
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

prim_one_iteration(graph, key, parent, mstSet)

print("key =", key)
print("parent =", parent)
