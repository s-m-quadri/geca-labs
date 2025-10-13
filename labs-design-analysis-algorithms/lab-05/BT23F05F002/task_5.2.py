"""
Background:
Prim's algorithm builds MST by adding one vertex at a time.

Task:
Write a function to find the vertex with the minimum key not yet in MST.

Instruction:
- Input: key[], mstSet[]
- Output: index of minimum key vertex.

Tip:
Use a simple linear search.

Test case:
key = [0, 2, 3]
mstSet = [True, False, False]
# Expected output: 1
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

key = [0, 2, 3]
mstSet = [True, False, False]
result = find_min_key_vertex(key, mstSet)
print(f"Test case 1:")
print(f"key = {key}")
print(f"mstSet = {mstSet}")
print(f"Minimum key vertex: {result}")
print(f"Expected: 1, Got: {result}")

print("\nTest case 2:")
key2 = [float('inf'), 5, 1, 8, 3]
mstSet2 = [False, True, False, True, False]
result2 = find_min_key_vertex(key2, mstSet2)
print(f"key = {key2}")
print(f"mstSet = {mstSet2}")
print(f"Minimum key vertex: {result2}")
print(f"Expected: 2 (key=1), Got: {result2}")

print("\nTest case 3:")
key3 = [0, 4, 2, 7]
mstSet3 = [True, False, False, False]
result3 = find_min_key_vertex(key3, mstSet3)
print(f"key = {key3}")
print(f"mstSet = {mstSet3}")
print(f"Minimum key vertex: {result3}")
print(f"Expected: 2 (key=2), Got: {result3}")

print("\nTest case 4 - All vertices in MST:")
key4 = [0, 2, 3]
mstSet4 = [True, True, True]
result4 = find_min_key_vertex(key4, mstSet4)
print(f"key = {key4}")
print(f"mstSet = {mstSet4}")
print(f"Minimum key vertex: {result4}")
print(f"Expected: -1 (no vertex available), Got: {result4}")
