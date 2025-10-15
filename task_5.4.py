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
def prim_iteration(graph, key, parent, mstSet):
    # Step 1: Pick the vertex with minimum key not yet in MST
    n = len(graph)
    min_value = float('inf')
    u = -1
    for v in range(n):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            u = v

    # Include vertex u in MST
    mstSet[u] = True

    # Step 2: Update key[] and parent[] for neighbors of u
    for v in range(n):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

# Test case
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

prim_iteration(graph, key, parent, mstSet)

print("After one iteration:")
print("Key:", key)
print("Parent:", parent)
print("MST Set:", mstSet)
