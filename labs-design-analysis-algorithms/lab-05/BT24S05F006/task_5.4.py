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

def primIteration(graph, key, mstSet, parent):
    # Step 1: Select the min-key vertex
    min_val = float('inf')
    u = -1
    for v in range(len(graph)):
        if mstSet[v] == False and key[v] < min_val:
            min_val = key[v]
            u = v

    # Step 2: Mark it as included
    mstSet[u] = True

    # Step 3: Update neighbors
    for v in range(len(graph)):
        if graph[u][v] != 0 and mstSet[v] == False and graph[u][v] < key[v]:
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

primIteration(graph, key, mstSet, parent)

print("key:", key)       # Expected: [0, 1, 2]
print("parent:", parent) # Expected: [-1, 0, 1]
