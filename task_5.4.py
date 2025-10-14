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
    # Find the min-key vertex not yet in MST
    min_index = -1
    min_val = float('inf')
    for i in range(len(key)):
        if not mstSet[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i
    u = min_index
    mstSet[u] = True
    # Update keys and parents for neighbors
    for v in range(len(graph)):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    key = [0, float('inf'), float('inf')]
    mstSet = [True, False, False]
    parent = [-1, -1, -1]
    prim_iteration(graph, key, parent, mstSet)
    print("key =", key)
    print("parent =", parent)
