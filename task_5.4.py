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
def find_min_key_vertex(key, mstSet):
    V = len(key)
    min_key = float('inf')
    min_index = -1
    
    for v in range(V):
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v
    
    return min_index

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    
    for v in range(V):
        if (not mstSet[v] and 
            graph[u][v] != 0 and 
            graph[u][v] < key[v]):
            key[v] = graph[u][v]
            parent[v] = u

def prim_iteration(graph, key, parent, mstSet):
    u = find_min_key_vertex(key, mstSet)
    
    if u == -1:
        return None
    
    mstSet[u] = True
    
    update_keys(graph, u, key, parent, mstSet)
    
    return u

graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, float('inf'), float('inf')]
mstSet = [True, False, False]
parent = [-1, -1, -1]

print("Initial state:")
print(f"graph = {graph}")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")

selected_vertex = prim_iteration(graph, key, parent, mstSet)

print(f"\nAfter one iteration:")
print(f"Selected vertex: {selected_vertex}")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")
print(f"Expected key = [0, 1, 2]")
print(f"Expected parent = [-1, 0, 1]")

print("\nTest case 2 - Second iteration:")
selected_vertex2 = prim_iteration(graph, key, parent, mstSet)
print(f"Selected vertex: {selected_vertex2}")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")

print("\nTest case 3 - Third iteration:")
selected_vertex3 = prim_iteration(graph, key, parent, mstSet)
print(f"Selected vertex: {selected_vertex3}")
print(f"key = {key}")
print(f"parent = {parent}")
print(f"mstSet = {mstSet}")

print("\nTest case 4 - No more vertices:")
selected_vertex4 = prim_iteration(graph, key, parent, mstSet)
print(f"Selected vertex: {selected_vertex4} (should be None)")

print("\nMST edges found:")
for v in range(len(parent)):
    if parent[v] != -1:
        weight = graph[v][parent[v]]
        print(f"Edge: ({parent[v]}, {v}) with weight {weight}")