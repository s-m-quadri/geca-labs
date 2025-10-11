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

def prim_mst(graph):
    V = len(graph)
    
  
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    key[0] = 0
    
    for _ in range(V):
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True
        
       
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    return parent, key

def min_key_vertex(key, mstSet):
    min_value = float('inf')
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    return min_index


# Example 
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]

parent, key = prim_mst(graph)

print("Edge \tWeight")
for i in range(1, len(graph)):
    print(f"{parent[i]} - {i} \t{key[i]}")

