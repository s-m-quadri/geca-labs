def min_key_vertex(key, mstSet):
    """
    Find the vertex with the minimum key value not yet included in MST.

    key: list of key values
    mstSet: list of booleans indicating vertices included in MST
    Returns: index of vertex with minimum key
    """
    min_val = float('inf')
    min_index = -1

    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index
#tests
# Test case
key = [0, 2, 3]
mstSet = [True, False, False]
result = min_key_vertex(key, mstSet)
print("Vertex with minimum key not in MST:", result)

