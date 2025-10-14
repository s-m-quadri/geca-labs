def min_key_vertex(key, mstSet):
    """
    Find the vertex with the minimum key value not yet included in MST.

    Parameters:
    key : list
        List of key values for each vertex.
    mstSet : list
        Boolean list indicating inclusion in MST.

    Returns:
    int
        Index of the vertex with minimum key not in MST.
    """
    min_value = float('inf')
    min_index = -1

    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v

    return min_index

# Test case
key = [0, 2, 3]
mstSet = [True, False, False]

print("Minimum key vertex:", min_key_vertex(key, mstSet))
