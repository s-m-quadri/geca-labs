"""
Background:
After picking a vertex, we update keys of adjacent vertices.

Task:
Implement a function to update key[] and parent[] for neighbors of selected vertex.

Instruction:
- Input: graph (adjacency matrix), u (selected vertex), key[], parent[], mstSet[]
- Update key[v] if edge weight is smaller.

Tip:
Skip vertices already in mstSet.

Test case:
graph = [
 [0, 2, 0],
 [2, 0, 3],
 [0, 3, 0]
]
u = 0
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after update:
# key = [0, 2, ∞]
# parent = [-1, 0, -1]
"""
def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    
    for v in range(V):
        if (not mstSet[v] and 
            graph[u][v] != 0 and 
            graph[u][v] < key[v]):
            key[v] = graph[u][v]
            parent[v] = u

graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]
u = 0
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

print("Before update:")
print(f"graph = {graph}")
print(f"Selected vertex u = {u}")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")

update_keys(graph, u, key, parent, mstSet)

print("\nAfter update:")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"Expected key = [0, 2, inf]")
print(f"Expected parent = [-1, 0, -1]")

print("\nTest case 2 - More complex graph:")
graph2 = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 3],
    [0, 5, 3, 0]
]
u2 = 1
key2 = [1, 0, float('inf'), float('inf')]
mstSet2 = [False, True, False, False]
parent2 = [1, -1, -1, -1]

print(f"\nBefore update (vertex {u2}):")
print(f"key = {key2}")
print(f"parent = {parent2}")
print(f"mstSet = {mstSet2}")

update_keys(graph2, u2, key2, parent2, mstSet2)

print(f"\nAfter update:")
print(f"key = {key2}")
print(f"parent = {parent2}")
print("Vertex 1 is connected to vertices 0,2,3 with weights 1,2,5")
print("Expected updates: key[2]=2, parent[2]=1, key[3]=5, parent[3]=1")